import click
from sqlalchemy.orm.session import Session

from models import Client, Contract, Event
from utils import prompt_options, use_session

from controllers.permissions import get_permissions


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
        return "main", user

    def support_menu(self, user):
        return "main", user

    def commercial_menu(self, user):
        return "main", user

    def manager_menu(self, user):
        return "main", user
