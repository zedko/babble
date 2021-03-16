import pytest

from babbler import app, db
from babbler.models import User, Message


@pytest.fixture(scope="session")
def app_fixture():
    app.config["TESTING"] = True
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost:5432/pytest"
    return app


@pytest.fixture(scope="session")
def client_fixture(app_fixture):
    with app_fixture.app_context():
        client = app.test_client()
        yield client


@pytest.fixture(scope="session")
def db_fixture(app_fixture):
    db.init_app(app_fixture)
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope="module")
def user_fixture(db_fixture):
    test_user = User.create_user({"email": "test@test.ru"})
    db.session.add(test_user)
    db.session.commit()
    yield test_user
    db.session.remove()




