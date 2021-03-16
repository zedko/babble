from requests import post


class Sender:
    """
    Handles sending of messages
    """
    def __init__(self, send_from=__name__, send_to="http://127.0.0.1:5000/report/"):
        """
        :param send_from: provide a module name
        :param send_to: url that will wait for POST with JSON to come
        """
        self._send_to = send_to
        self._send_from = send_from
        self.data = {
            "from": self._send_from,
            "message": '',
            "importance": '',
        }

    def send(self, message: str, importance: str = 'debug') -> None:
        """
        Call to make a POST request
        :param importance: could be one of ['debug', 'info', 'error']
        :param message:  JSON serialized sting
        :return:
        """
        self.data['message'] = message
        self.data['importance'] = importance
        post(self._send_to, json=self.data)


if __name__ == '__main__':
    send = Sender()
    send.send("error help me")