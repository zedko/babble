import re

from babbler.babbler import Babbler
from babbler.models import User, Message
from babbler.notifiers import ConsoleNotifier


def test_get_user(user_fixture):
    pk = user_fixture.uuid
    user_from_db = User.query.get(pk)
    assert user_from_db.uuid == user_fixture.uuid
    assert user_from_db is user_fixture


def test_console_message_via_babbler(user_fixture, capsys):
    """
    Message should be written to database and sent to stdout/stderr
    """
    # setup Babbler
    babbler = Babbler()
    babbler.setup(user_uuid=user_fixture.uuid)
    babbler.add_notifier(ConsoleNotifier())

    # send messages and catch console output
    babbler.babble("test debug", importance="debug")
    babbler.babble("test error", importance="error")
    captured = capsys.readouterr()

    # setup patterns for Message.__str__ '{self.importance} --> Message {self.id} from {self.source} \n{self.message}'
    pattern = re.compile(r'((debug|info|error) --> Message \d* from [\w.]+ \n.*)')

    assert re.match(pattern, captured.out)
    assert re.match(pattern, captured.err)

