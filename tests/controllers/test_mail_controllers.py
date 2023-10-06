from controllers.mail_control import check_mail_is_valid, check_mail_is_in_db
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


def test_check_mail_is_valid():
    assert check_mail_is_valid("a@b.com") == (True, [])


def test_check_mail_is_invalid_no_point():
    assert check_mail_is_valid("a@b") == (
        False,
        ["Mail must contain at least one .", "Mail must end with .com, .fr or .net"],
    )


def test_check_mail_is_invalid_too_many_at():
    assert check_mail_is_valid("a@@b.com") == (False, ["Mail must contain only one @"])


def test_check_mail_is_in_db_no_mail_in_db():
    # [TODO] Check if the mail is in the database
    db_session = UnifiedAlchemyMagicMock()
    db_session.query.return_value.all.return_value = []

    mock_res = check_mail_is_in_db(mail="a@b.com")
    assert (mock_res, [1, 2, 3])
