from typing import List, Tuple

def check_password_is_valid(password: str, password_confirmation) -> Tuple[bool, List[str]]:
    """Check if the password is valid and return a list of errors if not (is_valid, errors)"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter")
    if password != password_confirmation:
        errors.append("Password and password confirmation must be the same")

    if len(errors) > 0:
        return False, errors
    return True, errors
