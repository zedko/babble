from babbler.notifiers.notifier import Notifier


class Babbler:
    """
    This class coordinates what to do with messages

    Use notify method to:
    1) Trigger all notifications via Observer pattern
    2) Trigger logging message to DB

    Use add_notifier / remove_notifier to add / remove method of sending messages
    """

    def __init__(self, basic_importance: str = "debug"):
        self.notifiers = []
        self.basic_importance = basic_importance

    def babble(self, message: str, importance: str = None):
        """
        Use this method to spread the message and log it to DB
        :param message: string that we want to share
        :param importance: can be ["debug","info","error"]
        :return: None
        """
        importance = importance or self.basic_importance
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
