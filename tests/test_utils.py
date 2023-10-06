from utils import use_session


@use_session
def test_use_session(session):
    assert session is not None
