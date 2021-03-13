import sys

from babbler.notifiers.notifier import Notifier


class ConsoleNotifier(Notifier):
    def debug_notify(self, message: str):
        print(message)

    def info_notify(self, message: str):
        print(message)

    def error_notify(self, message: str):
        print(message, file=sys.stderr)