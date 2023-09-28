from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)


# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)


# Create a base class for declarative models
Base = declarative_base()


# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    password = Column(String(50))


# Create the database tables
Base.metadata.create_all(engine)


def create_new_user(name, email, phone_number, password):
    """
    Create a new user ('name', 'email', 'phone_number', 'password')
    in the database and return it, if the user already exist return None
    """
    new_user = User(
        name=name, email=email, phone_number=phone_number, password=password
    )
    with Session.begin() as session:
        session.add(new_user)
    return new_user


# Query the database to retrieve the user
# retrieved_user = session.query(User).filter_by(username="john_doe").first()
# print(
#    f"User ID: {retrieved_user.id}, Username: {retrieved_user.username}, Email: {retrieved_user.email}, Full Name: {retrieved_user.full_name}"
# )
