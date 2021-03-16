import sys

from babbler.notifiers.notifier import Notifier
from babbler.models import Message


class ConsoleNotifier(Notifier):
    """
    Simply outputs notifications to stdout / stderr
    """
    def debug_notify(self, message: Message):
        print(message)

    def info_notify(self, message: Message):
        print(message)

    def error_notify(self, message: Message):
        print(message, file=sys.stderr)
