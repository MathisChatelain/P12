from faker import Faker

from models import User, Client, Contract, Event
from utils import prompt_options, use_session
from models.clients import create_new_client, update_client
from models.contracts import create_new_contract, update_contract
from models.events import create_new_event, update_event
from models.users import create_new_user, update_user
from controllers.permissions import get_permissions

import random

# Initialize Faker
fake = Faker()


def test_models_creation_without_data():
    assert User() is not None
    assert Client() is not None
    assert Contract() is not None
    assert Event() is not None


def test_create_new_user():
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    password = fake.password(length=8)  # Generate a random password
    is_superuser = random.choice([True, False])
    is_support = random.choice([True, False])
    is_manager = random.choice([True, False])
    is_commercial = random.choice([True, False])
    user = create_new_user(
        name=name,
        email=email,
        phone_number=phone_number,
        password=password,
        is_superuser=is_superuser,
        is_support=is_support,
        is_manager=is_manager,
        is_commercial=is_commercial,
    )
    assert user is not None
    assert user.name == name
    assert user.email == email


# do the same with the rest of the creates functions
def test_create_new_event_with_random_wrong_data():
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
    }
    user = create_new_event(data)
    assert user is not None
    assert hasattr(user, "name") is False
    assert hasattr(user, "email") is False
