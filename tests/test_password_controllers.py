from controllers.password_control import check_password_is_valid


def test_check_password_is_valid():
    password = "aBcDeFgH1"
    password_confirmation = "aBcDeFgH1"
    assert check_password_is_valid(password, password_confirmation) == (True, [])


def test_check_password_is_invalid_too_short():
    password = "aBcDe4g"
    password_confirmation = "aBcDe4g"
    assert check_password_is_valid(password, password_confirmation) == (
        False,
        ["Password must be at least 8 characters long"],
    )


def test_check_password_is_invalid_no_upper():
    password = "abcdefg1"
    password_confirmation = "abcdefg1"
    assert check_password_is_valid(password, password_confirmation) == (
        False,
        ["Password must contain at least one uppercase letter"],
    )


def test_check_password_is_invalid_no_lower():
    password = "ABCDEFG1"
    password_confirmation = "ABCDEFG1"
    assert check_password_is_valid(password, password_confirmation) == (
        False,
        ["Password must contain at least one lowercase letter"],
    )


def test_check_password_is_invalid_no_digit():
    password = "aBcDeFgH"
    password_confirmation = "aBcDeFgH"
    assert check_password_is_valid(password, password_confirmation) == (
        False,
        ["Password must contain at least one digit"],
    )


def test_check_password_is_invalid_not_same():
    password = "aBcDeFgH1"
    password_confirmation = "aBcDeFgH2"
    assert check_password_is_valid(password, password_confirmation) == (
        False,
        ["Password and password confirmation must be the same"],
    )
