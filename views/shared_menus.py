from utils import prompt_options, use_session
import click
from models.users import User
from models.clients import Client
from models.contracts import Contract
from models.events import Event
from views.menus import MainMenu


@use_session
def model_list(session, model, page=0):
    # TODO correctly display the model list
    return [str(model.id) for model in session.query(model).all()]


class SharedMenu:
    def __init__(self):
        pass

    def dashboards(self, user):
        click.echo("Dashboards")
        choice = prompt_options(
            ["Clients", "Contracts", "Events", "Users", "Else : Back"],
            callback=self.dashboards,
            clear=True,
            prompt="",
        )
        options = {0: Client, 1: Contract, 2: Event, 3: User}
        if model := options.get(choice):
            model_list(model)
        else:
            MainMenu.menu(user)

        # ● Tous les collaborateurs doivent pouvoir accéder à tous les clients,
        # contrats et événements en lecture seule.
        pass
