import click

from models.users import User
from utils import clear_terminal, use_session, prompt_options
from controllers.authentication import check_user_credentials
from models.users import create_new_user
from views.validations.mail_input_validation import mail_validation
from views.validations.password_input_validation import password_validation


@click.command()
@click.option("--mail", prompt="Mail")
@click.option("--name", prompt="Name")
@click.option("--password", prompt="Password")
@click.option("--password_confirmation", prompt="Password confirmation")
def signup(mail, name, password, password_confirmation):
    """Command that allow to create a new user"""
    mail = mail_validation(mail)
    password = password_validation(password, password_confirmation)
    phone_number = click.prompt("Phone number")
    create_new_user(
        name,
        mail,
        phone_number,
        password,
    )

    click.echo(f"{mail} : Hello {name}!, your password is {password}")


@click.command()
def login():
    """Command that allow to login"""
    mail = click.prompt("Mail")
    password = click.prompt("Password")
    user = check_user_credentials(mail, password)
    if user:
        main_menu(user)
    else:
        authentication_menu()


def authentication_menu():
    """Menu that allow to choose between login and signup"""
    choice = prompt_options(
        ["Login", "Sign Up"],
        callback=authentication_menu,
        clear=True,
        prompt="Authentication Menu\n",
    )
    match choice:
        case 0:
            login()
        case 1:
            signup()
        case _:
            # TODO add exception
            click.echo("Invalid choice")
