from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Boolean, Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy.sql import text

DB_PATH = f'./data.db'
DB_URL = f"sqlite:///data.db" # Define the database URL
Base = declarative_base()