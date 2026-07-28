import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # This Foreign Key strictly enforces that a user cannot be created 
    # unless the hostel_id matches a valid id in the 'hostels' table
    hostel_id = Column(UUID(as_uuid=True), ForeignKey("hostels.id"), nullable=False)
    
    role = Column(String, nullable=False)
    name = Column(String, nullable=False)
    room_number = Column(String, nullable=True)