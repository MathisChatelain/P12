import click
from controllers.mail_control import check_mail_is_in_db, check_mail_is_valid


def mail_validation(mail: str, session):
    mail_is_valid, mail_input_erros = check_mail_is_valid(mail)
    while mail_is_valid is False:
        # if the mail is not valid we display the errors
        click.echo(f"Mail is not valid :")
        for error in mail_input_erros:
            click.echo(f" - {error}")
        click.echo("")  # empty line

        # and we ask for a new mail
        mail = click.prompt("Mail")
        mail_is_valid, mail_input_erros = check_mail_is_valid(mail)

        if mail_is_valid:
            # we dont want to check if the mail is in the db if the mail is not valid
            if check_mail_is_in_db(session, mail):
                click.echo(f"There is already an account for thi mail")
                mail_is_valid = False

    return mail
