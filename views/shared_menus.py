from models.users import User
from utils import prompt_options, use_session
import click
from models.clients import Client
from models.contracts import Contract
from models.events import Event

@use_session
def model_list(session, model):
    # TODO correctly display the model list
    return [str(model.id) for model in session.query(model).all()]

def dashboards(user):
    # ● Tous les collaborateurs doivent pouvoir accéder à tous les clients,
    # contrats et événements en lecture seule.
    pass