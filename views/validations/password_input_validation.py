import click
from controllers.password_control import check_password_is_valid


def password_validation(password: str, password_confirmation: str):
    password_is_valid, password_input_erros = check_password_is_valid(
        password, password_confirmation
    )
    while password_is_valid is False:
        # if the password is not valid we display the errors
        click.echo(f"Password is not valid :")
        for error in password_input_erros:
            click.echo(f" - {error}")
        click.echo("")  # empty line

        # and we ask for a new password and password confirmation
        password = click.prompt("Password")
        password_confirmation = click.prompt("Password confirmation")

        password_is_valid, password_input_erros = check_password_is_valid(
            password, password_confirmation
        )

    return password
