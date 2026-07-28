import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Hostel(Base):
    # This tells SQLAlchemy the exact name of the table in PostgreSQL
    __tablename__ = "hostels"

    # UUID(as_uuid=True) ensures it generates a proper universally unique identifier
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    location_coords = Column(String, nullable=True)