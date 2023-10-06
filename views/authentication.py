import click
from sqlalchemy.orm import Session

from controllers.authentication import check_user_credentials
from models.users import create_new_user
from utils import prompt_options, use_session
from views.validations.mail_input_validation import mail_validation
from views.validations.password_input_validation import password_validation


@use_session
def signup(session: Session = Session(), connect=True):
    """Command that allow to create a new user"""
    mail = mail_validation(click.prompt("Mail"))
    name = click.prompt("Name")
    password = password_validation(
        click.prompt("Password"), click.prompt("Password confirmation")
    )
    phone_number = click.prompt("Phone number")
    user = create_new_user(
        session,
        name=name,
        email=mail,
        phone_number=phone_number,
        password=password,
    )

    if connect:
        click.echo(f"{mail} : Hello {name}!, your password is {password}")
    return "main", user


def login():
    """Command that allow to login"""
    mail = click.prompt("Mail")
    password = click.prompt("Password")
    user = check_user_credentials(mail=mail, password=password)
    if user:
        return "main", user
    else:
        return "authentication", None


class AuthenticationMenu:
    def __init__(self):
        pass

    def authentication(self):
        """Menu that allow to choose between login and signup"""
        choice = prompt_options(
            ["Login", "Sign Up", "Quit"],
            callback=self.authentication,
            clear=True,
            prompt="Authentication Menu\n",
        )
        if choice == 0:
            menu, user = login()
            return menu, user
        elif choice == 1:
            menu, user = signup()
            return menu, user
        elif choice == 2:
            return "exit", None
        else:
            # TODO add exception
            click.echo("Invalid choice")
            return "exit", None
