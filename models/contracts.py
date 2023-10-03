from sqlalchemy import (Boolean, Column, DateTime, Integer, Sequence, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base

from utils import use_session

# Define the SQLAlchemy database engine. We'll use SQLite for this example.
engine = create_engine("sqlite:///database.db", echo=True)

# Create a base class for declarative models
Base = declarative_base()


# Define the Contract model
class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, Sequence("contract_id_seq"), primary_key=True)
    client_id = Column(Integer)
    contact = Column(String(50))
    total_amount = Column(Integer, default=0)
    amount_to_pay = Column(Integer, default=0)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    status = Column(Boolean, default=False)

    def _to_repr(self):
        return str(f"Contract: {self.id}")


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_contract(session):
    """TODO"""
    new_contract = Contract()
    session.add(new_contract)
    return new_contract
