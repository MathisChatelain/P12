import click

# DB connection
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from views.validations.mail_input_validation import mail_validation
from views.validations.password_input_validation import password_validation

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

    click.echo(f"{mail} : Hello {name}!, your password is {password}")


if __name__ == "__main__":
    signup()
