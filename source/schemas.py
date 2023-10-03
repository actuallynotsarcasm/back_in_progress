from sqlalchemy import create_engine, String, Integer, Column, Float
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:Postgres_8614@localhost/vtb_autocredit")
Base = declarative_base()


class Cars(Base):
    __tablename__ = 'cars' 
    id = Column('id', Integer(), primary_key=True)
    slug = Column('car_slug', String(50),  nullable=False)
    brand = Column('brand', String(50),  nullable=False)
    model = Column('model', String(50),  nullable=False)
    complement = Column('complement', String(50),  nullable=False)
    photo_id = Column('photo_id', Integer(), nullable=True)
    price = Column('price', Float(), nullable=False)
    trade_in_profit = Column('trade_in_profit', Float(), nullable=False)
    credit_profit = Column('credit_profit', Float(), nullable=False)


class Dealers(Base):
    __tablename__ = 'dealers'
    id = Column('id', Integer(), primary_key=True)
    slug = Column('dealer_slug', String(50),  nullable=False)
    name = Column('name', String(50),  nullable=False)
    address = Column('address', String(50),  nullable=False)


class Moderators(Base):
    __tablename__ = 'moderators'
    id = Column('id', Integer(), primary_key=True)
    dealer_id = Column('dealer_id', Integer(),  nullable=False)
    name = Column('name', String(50),  nullable=False)
    surname = Column('surname', String(50),  nullable=False)
