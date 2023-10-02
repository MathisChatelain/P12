import os

import click
from sqlalchemy import create_engine, orm

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
# expire_on_commit=False is used to keep the session alive after a commit
SessionLocal = orm.sessionmaker(bind=engine, expire_on_commit=False)


def use_session(func):
    """Decorator that provide a session to the decorated function and autoclose it"""

    def wrapper(*args, **kwargs):
        # Create a session
        session = SessionLocal()

        try:
            # Pass the session to the decorated function
            result = func(session, *args, **kwargs)
            session.commit()  # Commit the changes to the database
        except Exception as e:
            session.rollback()  # Rollback in case of an exception
            raise e
        finally:
            session.close()  # Close the session

        return result

    return wrapper


def clear_terminal():
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")


def prompt_options(
    options: list,
    prompt: str = "Please select an option by typing it's number\n",
    clear: bool = False,
    callback=None,
    errors=[],
):
    """Prompt the user to choose an option from a list of options"""

    if clear:
        clear_terminal()

    for error in errors:
        click.echo(error)
    click.echo(prompt)
    for i, option in enumerate(options):
        click.echo(f"{i}: {option}\n")
    choice = click.prompt("-->", type=int)
    if choice in range(len(options)):
        return choice
    else:
        if callback:
            callback()
        else:
            return prompt_options(options, prompt, clear, callback, ["Invalid choice"])
