import json

from models.users import create_new_user
from utils import use_session
from sqlalchemy import create_engine, orm

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
# expire_on_commit=False is used to keep the session alive after a commit
SessionLocal = orm.sessionmaker(bind=engine, expire_on_commit=False)
session = SessionLocal()

with open("mocks/mock_users.json", 'r') as file:
    users_data = json.load(file)

    for user_data in users_data:
        name = user_data['name']
        email = user_data['email']
        phone_number = user_data['phone_number']
        password = user_data['password']
        create_new_user(session,name=name, email=email, phone_number=phone_number, password=password)

session.commit()
session.close()
