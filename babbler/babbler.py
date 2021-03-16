from babbler.notifiers.notifier import Notifier
from babbler.models import User, Message


class Babbler:
    """
    This class coordinates what to do with messages
    Add some noti
    Use self.babble method to send

    Use notify method to:
    1) Trigger all notifications via Observer pattern
    2) Trigger logging message to DB

    Use add_notifier / remove_notifier to add / remove method of sending messages

    """
    user_uuid = None
    source = __name__
    basic_importance = "error"

    @classmethod
    def setup(cls, user_uuid: str = None, source: str = None, basic_importance: str = None) -> None:
        """
        Setting up params of a class
        :param user_uuid: your uuid as str
        :param source: this will be shown as "Source" of your message
        :param basic_importance: basic importance for all messages
        :return: None
        """
        cls.user_uuid = user_uuid or cls.user_uuid
        cls.source = source or cls.source
        cls.basic_importance = basic_importance or cls.basic_importance

    def __init__(self):
        self.notifiers = []

    def babble(self, message: str, importance: str = None):
        """
        Use this method to spread the message and log it to DB
        :param message: string that we want to share
        :param importance: optional.  can be set ["debug","info","error"] to one time call
        :return: None
        """
        importance = importance or Babbler.basic_importance

        # Create Message and save it to database
        message = Message.create_message(source=Babbler.source, message=message,
                                         importance=importance, user_uuid=Babbler.user_uuid)
        for notifier in self.notifiers:
            notifier.notify(message, importance)

    def add_notifier(self, notifier: Notifier) -> None:
        if notifier in self.notifiers:
            return None
        self.notifiers.append(notifier)

    def remove_notifier(self, notifier: Notifier) -> None:
        try:
            self.notifiers.remove(notifier)
        except ValueError:
            self.babble(f"Cannot remove notifier {notifier}")
