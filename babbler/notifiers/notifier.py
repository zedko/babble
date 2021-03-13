from abc import ABC, abstractmethod


class Notifier(ABC):
    @property
    def deliver_methods(self):
        methods = {
            "debug": self.debug_notify,
            "info": self.info_notify,
            "error": self.error_notify,
        }
        return methods

    def notify(self, message: str, importance: str) -> None:
        """
        Delivers a message via subclasses unique way
        :param importance: can be ["debug","info","error"]
        :param message: str message to deliver
        :return: None
        """
        try:
            method = self.deliver_methods[importance]
            method(message)
        except KeyError as e:
            raise KeyError(f'Cannot use importance {e},'
                           f' importance param should be one of {list(self.deliver_methods.keys())}')

    @abstractmethod
    def debug_notify(self, message: str):
        pass

    @abstractmethod
    def info_notify(self, message: str):
        pass

    @abstractmethod
    def error_notify(self, message: str):
        pass




