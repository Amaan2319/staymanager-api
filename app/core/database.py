import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Get the database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Create the Engine (The core interface to the database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. Create a SessionLocal class (Each instance of this will be an actual database session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Create a Base class (All our future database models will inherit from this)
Base = declarative_base()
# 6. Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()