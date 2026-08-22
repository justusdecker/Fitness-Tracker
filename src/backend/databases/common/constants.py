from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import text

DB_PATH = f'./data/lprt_data.db'
DB_URL = f"sqlite:///./lprt_data.db" # Define the database URL
Base = declarative_base()