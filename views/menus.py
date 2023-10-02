import click

from models.users import User
from utils import clear_terminal, use_session, prompt_options
from views.authentication import authentication_menu


def main_menu(user: User):
    """Menu that allow to choose between the main commands of the application"""
    phrase = f"Main Menu\nYou are connected as {user.name}\n"
    choice = prompt_options(
        ["Create a new task", "Show all tasks", "Logout"],
        callback=main_menu,
        clear=True,
        prompt=phrase,
    )
    match choice:
        case 0:
            # TODO add create task command
            pass
        case 1:
            # TODO add show all tasks command
            pass
        case 2:
            authentication_menu()
        case _:
            # TODO add exception
            click.echo("Invalid choice")
    click.pause("Press any key to continue...")
