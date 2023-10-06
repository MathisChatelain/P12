from sqlalchemy import Boolean, Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20), unique=True)
    password = Column(String(50))
    is_superuser = Column(Boolean, default=False)
    is_support = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    is_commercial = Column(Boolean, default=False)

    def _to_repr(self):
        return str(f"User: {self.name} at {self.email}")

    def data_to_str(self):
        return [
            f"{key}: {value}"
            for key, value in self.__dict__.items()
            if isinstance(value, bool) is False
        ]


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_user(
    session,
    name,
    email,
    phone_number,
    password,
    is_superuser=False,
    is_support=False,
    is_manager=False,
    is_commercial=False,
):
    """
    Create a new user ('name', 'email', 'phone_number', 'password')
    in the database and return it, if the user already exist return None
    """
    new_user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        password=password,
        is_superuser=is_superuser,
        is_support=is_support,
        is_manager=is_manager,
        is_commercial=is_commercial,
    )
    session.add(new_user)
    return new_user


@use_session
def update_user(session, user: User, **kwargs):
    """
    Update a user with the new values in kwargs
    """
    for key, value in kwargs.items():
        setattr(user, key, value)
    session.update(user)
    return user


@use_session
def get_user_from_key(session: Session = Session(), key=""):
    user = session.query(User).filter(User.id == key).first()
    for field in ["name", "email", "phone_number"]:
        if user:
            return user
        user = session.query(User).filter(getattr(User, field) == key).first()
    return None
