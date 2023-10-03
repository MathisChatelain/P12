import click
from sqlalchemy.orm.session import Session

from models import Client, Contract, Event, User
from utils import prompt_options, use_session


@use_session
def model_list(model, page=0 , session: Session=Session()):
    # TODO correctly display the model list
    return [str(model.id) for model in session.query(model).all()]


class SharedMenu:
    def __init__(self):
        pass

    def dashboards(self, user):
        click.echo("Dashboards")
        choice: int = prompt_options(
            ["Clients", "Contracts", "Events", "Users", "Else : Back"],
            callback=self.dashboards,
            clear=True,
            prompt="",
        )
        options = {0: Client, 1: Contract, 2: Event, 3: User}
        if model := options.get(choice):
            model_list(model=model)
        else:
            return "main", user

        # ● Tous les collaborateurs doivent pouvoir accéder à tous les clients,
        # contrats et événements en lecture seule.
        pass
