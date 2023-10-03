import click
from sqlalchemy.orm import Session

from models import User
from utils import use_session


@use_session
def check_user_credentials(mail: str, password: str, session: Session = Session()):
    """Check if the mail and password match an user in the database"""
    user = (
        session.query(User)
        .filter(User.email == mail)
        .filter(User.password == password)
        .first()
    )
    if user:
        click.echo(f"{mail} : Hello you are logged in!")
        return user
    click.echo("Mail or password is incorrect, please try again\n")
    return None
