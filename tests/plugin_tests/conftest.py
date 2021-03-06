import pytest
from mock import patch
from responses import RequestsMock
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


@pytest.fixture()
def mock_requests():
    with RequestsMock() as reqs:
        yield reqs


class MockDB:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = scoped_session(sessionmaker(self.engine))


@pytest.fixture()
def mock_db():
    return MockDB()


@pytest.fixture
def patch_paste():
    with patch('cloudbot.util.web.paste') as mock:
        yield mock


@pytest.fixture()
def patch_try_shorten():
    with patch('cloudbot.util.web.try_shorten', new=lambda x: x):
        yield


@pytest.fixture()
def unset_bot():
    yield
    from cloudbot.bot import bot
    bot.set(None)
