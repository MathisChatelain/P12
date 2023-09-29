import os

from sqlalchemy import create_engine, orm

db_url = "sqlite:///database.db"
engine = create_engine(db_url)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def use_session(func):
    """Decorator that provide a session to the decorated function and autoclose it"""

    def wrapper(*args, **kwargs):
        # Create a session
        session = SessionLocal()

        try:
            # Pass the session to the decorated function
            result = func(session, *args, **kwargs)
            session.commit()  # Commit the changes to the database
        except Exception as e:
            session.rollback()  # Rollback in case of an exception
            raise e
        finally:
            session.close()  # Close the session

        return result

    return wrapper


def clear_terminal():
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")
