from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    Sequence,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False)
    status = Column(Boolean, default=False)

    def _to_repr(self):
        return str(f"Contract: {self.id}")

    def data_to_str(self):
        return [
            f"{key}: {value}"
            for key, value in self.__dict__.items()
            if type(value) != bool
        ]


# Create the database tables
Base.metadata.create_all(engine)


@use_session
def create_new_contract(
    session,
    client_id,
    contact="",
    total_amount=0,
    amount_to_pay=0,
    status=False,
):
    created_at = datetime.now()
    updated_at = datetime.now()
    new_contract = Contract(
        client_id=client_id,
        contact=contact,
        total_amount=total_amount,
        amount_to_pay=amount_to_pay,
        created_at=created_at,
        updated_at=updated_at,
        status=status,
    )
    session.add(new_contract)
    return new_contract


@use_session
def update_contract(session, contract, **kwargs):
    """
    Update a contract with the new values in kwargs
    """
    for key, value in kwargs.items():
        if hasattr(contract, key) and key not in ["id", "created_at", "updated_at"]:
            setattr(contract, key, value)
        setattr(contract, "updated_at", datetime.now())
    return contract
