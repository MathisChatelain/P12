import click

from models.users import User
from utils import clear_terminal, prompt_options


class MainMenu:
    def __init__(self):
        pass

    def menu(self, user: User):
        """Menu that allow to choose between the main commands of the application"""
        phrase = f"Main Menu\nYou are connected as {user.name}\n"
        choice = prompt_options(
            ["Show dashboards (readonly)", "Show my actions", "Exit"],
            callback=self.menu,
            clear=True,
            prompt=phrase,
        )
        if choice == 0:
            return "dashboards", user
        elif choice == 1:
            return "action_menu", user
        elif choice == 2:
            return "authentication", None
        elif choice == 3:
            clear_terminal()
            click.echo("Goodbye!")
            exit()
        else:
            # TODO add exception
            click.echo("Invalid choice")
            return "exit", None
