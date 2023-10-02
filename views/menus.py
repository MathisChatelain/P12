import click

from models.users import User
from utils import clear_terminal, prompt_options, use_session

try:
    from views.authentication import AuthenticationMenu
except ImportError:
    pass

try:
    from views.shared_menus import SharedMenu
except ImportError:
    pass


class MainMenu:
    def __init__(self):
        pass

    def menu(self, user: User):
        """Menu that allow to choose between the main commands of the application"""
        phrase = f"Main Menu\nYou are connected as {user.name}\n"
        choice = prompt_options(
            ["Show dashboards", "Show all tasks", "Exit"],
            callback=self.menu,
            clear=True,
            prompt=phrase,
        )
        if choice == 0:
            SharedMenu.dashboards(user)
        elif choice == 1:
            # TODO add show all tasks command
            pass
        elif choice == 2:
            AuthenticationMenu.authentication()
        elif choice == 3:
            clear_terminal()
            click.echo("Goodbye!")
            exit()
        else:
            # TODO add exception
            click.echo("Invalid choice")
        click.pause("Press any key to continue...")
