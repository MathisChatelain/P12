from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine('sqlite:///database.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    full_name = Column(String(100))

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user
new_user = User(username='john_doe', email='john@example.com', full_name='John Doe')
session.add(new_user)
session.commit()

# Query the database to retrieve the user
retrieved_user = session.query(User).filter_by(username='john_doe').first()
print(f"User ID: {retrieved_user.id}, Username: {retrieved_user.username}, Email: {retrieved_user.email}, Full Name: {retrieved_user.full_name}")

# Close the session
session.close()

