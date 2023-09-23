def check_mail_is_valid(mail: str) -> (bool, [str]):
    """Check if the mail is valid and return a list of errors if not (is_valid, errors)"""
    errors = []

    if mail.count("@") != 1:
        errors.append("Mail must contain only one @")
    if mail.count(".") == 0:
        errors.append("Mail must contain at least one .")
    if mail.split(".")[-1] not in ["com", "fr", "net"]:
        errors.append("Mail must end with .com, .fr or .net")

    if len(errors) > 0:
        return False, errors
    return True, errors


def check_mail_is_in_db(session, mail: str) -> bool:
    """Check if the mail is in the database and return a list of errors if not (is_valid, errors)"""
    # [TODO] Check if the mail is in the database
    return False
