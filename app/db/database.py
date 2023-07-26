from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

base = os.getenv('BASE')
drivername = os.getenv('DRIVERNAME')
username = os.getenv('USERNAME')
password = os.getenv("PASSWORD")
connection = os.getenv('CONNECTION')
database = os.getenv('DATABASE')

SQLALCHEMY_DATABASE_URL = f"{base}+{drivername}://{username}:{password}@{connection}/{database}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()