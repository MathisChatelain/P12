from controllers.mail_control import check_mail_is_valid


def test_check_mail_is_valid():
    assert check_mail_is_valid("a@b.com") == (True, [])


def test_check_mail_is_invalid_no_point():
    assert check_mail_is_valid("a@b") == (
        False,
        ["Mail must contain at least one .", "Mail must end with .com, .fr or .net"],
    )


def test_check_mail_is_invalid_too_many_at():
    assert check_mail_is_valid("a@@b.com") == (False, ["Mail must contain only one @"])
