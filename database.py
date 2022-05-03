from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABSE_URL="mysql+pymysql://root:@127.0.0.1/todo"

engine=create_engine(
    SQLALCHEMY_DATABSE_URL
)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()