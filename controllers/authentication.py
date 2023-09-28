from utils import use_session
from models.users import User
import click


@use_session
def check_user_credentials(session, mail, password):
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
