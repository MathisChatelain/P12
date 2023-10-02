import click

from models.users import User
from utils import clear_terminal, prompt_options, use_session
from views.authentication import authentication_menu
from views.shared_menus import dashboards


def main_menu(user: User):
    """Menu that allow to choose between the main commands of the application"""
    phrase = f"Main Menu\nYou are connected as {user.name}\n"
    choice = prompt_options(
        ["Show dashboards", "Show all tasks", "Logout", "Exit"],
        callback=main_menu,
        clear=True,
        prompt=phrase,
    )
    if choice == 0:
        dashboards(user)
    elif choice == 1:
        # TODO add show all tasks command
        pass
    elif choice == 2:
        authentication_menu()
    elif choice == 3:
        clear_terminal()
        click.echo("Goodbye!")
        exit()
    else:
        # TODO add exception
        click.echo("Invalid choice")
    click.pause("Press any key to continue...")
