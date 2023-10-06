import click
from sqlalchemy.orm.session import Session

from controllers.permissions import get_permissions
from models import Client, Contract, Event, User
from models.users import get_user_from_key
from utils import prompt_options, use_session
from views.authentication import signup


@use_session
def model_list(model, page=0, session: Session = Session()):
    # TODO correctly display the model list
    return [model._to_repr() for model in session.query(model).all()]


class SharedMenu:
    def __init__(self):
        pass

    def dashboards(self, user):
        click.echo("Dashboards")
        choice: int = prompt_options(
            ["Clients", "Contracts", "Events", "Else : Back"],
            callback=self.dashboards,
            clear=True,
            prompt="",
        )
        options = {0: Client, 1: Contract, 2: Event}
        if model := options.get(choice):
            elements = model_list(model=model)
            for index, elem in enumerate(elements):
                click.echo(f"{index} - {elem}")
            else:
                click.echo("No elements found")
            click.pause("Press any key to continue...")
            return "dashboards", user
        else:
            return "main", user


class ActionMenu:
    def __init__(self):
        pass

    def menu(self, user):
        role = get_permissions(user)
        if role == "superuser":
            return self.superuser_menu(user)
        elif role == "support":
            return self.support_menu(user)
        elif role == "commercial":
            return self.commercial_menu(user)
        elif role == "manager":
            return self.manager_menu(user)
        return "main", user

    def superuser_menu(self, user):
        """This is a sub menu only accessible by superuser, it allows to select any of the roles to impersonate"""
        click.echo("Superuser sub-menu")
        choice: int = prompt_options(
            ["Support menu", "Commercial menu", "Manager menu", "Else : Back"],
            callback=self.superuser_menu,
            clear=True,
            prompt="",
        )
        if choice == 0:
            return self.support_menu(user)
        elif choice == 1:
            return self.commercial_menu(user)
        elif choice == 2:
            return self.manager_menu(user)
        else:
            return "action_menu", user

    def support_menu(self, user):
        click.echo("Support menu")
        choice: int = prompt_options(
            ["Show events", "Update my events", "Else : Back"],
            callback=self.support_menu,
            clear=True,
            prompt="",
        )
        if choice == 0:
            # TODO add show events command
            return "support_menu", user
        elif choice == 1:
            # TODO add update my events command
            return "support_menu", user
        else:
            return "action_menu", user

    def commercial_menu(self, user):
        return "main", user

    def manager_menu(self, user):
        click.echo("Manager menu")
        choice: int = prompt_options(
            ["Create user", "Update user", "Show events", "Else : Back"],
            callback=self.manager_menu,
            clear=True,
            prompt="",
        )
        if choice == 0:
            # This creates a new user without connecting it
            _, new_user = signup(connect=False)
            click.echo(f"User {new_user.name} created")
            click.pause("Press any key to continue...")
            return "manager_menu", user

        elif choice == 1:
            # TODO add update user command
            user_key = click.prompt(
                "Select user to update (you can use mail, id, phone number or name)"
            )
            user_to_update = get_user_from_key(key=user_key)
            if user_to_update:
                user_to_update: User
                click.echo(f"User {user_to_update.name} found")
                for field in user_to_update.data_to_str():
                    click.echo(field)
                # TODO add update user command
            else:
                click.echo("No user found with any of the given keys")

            return "manager_menu", user

        elif choice == 2:
            # TODO add show events command
            return "manager_menu", user

        else:
            return "action_menu", user
