import click

# DB connection
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from views.validations.mail_input_validation import mail_validation
from views.validations.password_input_validation import password_validation
from controllers.authentication import check_user_credentials

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
session = Session(engine)


@click.command()
@click.option("--mail", prompt="Mail")
@click.option("--name", prompt="Name")
@click.option("--password", prompt="Password")
@click.option("--password_confirmation", prompt="Password confirmation")
def signup(mail, name, password, password_confirmation):
    """Command that allow to create a new user"""
    mail = mail_validation(mail, session)
    password = password_validation(password, password_confirmation)

    # [TODO] Create the user in the database

    click.echo(f"{mail} : Hello {name}!, your password is {password}")


@click.command()
@click.option("--mail", prompt="Mail")
@click.option("--password", prompt="Password")
def login(mail, password):
    """Command that allow to login"""
    user = None
    while not user:
        mail = mail_validation(mail, session)
        password = password_validation(password, password)
        user = check_user_credentials(mail, password)

    click.echo(f"{mail} : Hello you are logged in!")
