import click

from controllers.authentication import check_user_credentials
from models.users import User, create_new_user
from utils import clear_terminal, prompt_options, use_session
from views import MainMenu if 
from views.validations.mail_input_validation import mail_validation
from views.validations.password_input_validation import password_validation


@click.command()
@click.option("--mail", prompt="Mail")
@click.option("--name", prompt="Name")
@click.option("--password", prompt="Password")
@click.option("--password_confirmation", prompt="Password confirmation")
@use_session
def signup(session,mail, name, password, password_confirmation):
    """Command that allow to create a new user"""
    mail = mail_validation(mail)
    password = password_validation(password, password_confirmation)
    phone_number = click.prompt("Phone number")
    user = create_new_user(
        session,
        name=name,
        email=mail,
        phone_number=phone_number,
        password=password,
    )

    click.echo(f"{mail} : Hello {name}!, your password is {password}")
    MainMenu().menu(user)


@click.command()
def login():
    """Command that allow to login"""
    mail = click.prompt("Mail")
    password = click.prompt("Password")
    user = check_user_credentials(mail=mail, password=password)
    if user:
        MainMenu().menu(user)
    else:
        AuthenticationMenu().authentication()


class AuthenticationMenu:
    def __init__(self):
        pass

    def authentication(self):
        """Menu that allow to choose between login and signup"""
        choice = prompt_options(
            ["Login", "Sign Up"],
            callback=self.authentication,
            clear=True,
            prompt="Authentication Menu\n",
        )
        if choice == 0:
            login()
        elif choice == 1:
            signup()
        else:
            # TODO add exception
            click.echo("Invalid choice")
