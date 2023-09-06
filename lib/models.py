from sqlalchemy import *
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///listings.db', echo=True)

Base = declarative_base()

class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    
    commercial_properties = relationship('CommercialProperty', backref='agent')
    residential_properties = relationship('ResidentialProperty', backref='agent')

class CommercialProperty(Base):
    __tablename__ = 'commercial_properties'
    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    address = Column(String)
    city = Column(String)
    area = Column(String) # estate or neighborhood
    type = Column(String)
    grade = Column(String)
    price_per_sqf = Column(Integer)
    agent_id = Column(String, ForeignKey('agents.id'))

class ResidentialProperty(Base):
    __tablename__ = 'residential_properties'
    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    address = Column(String)
    city = Column(String)
    area = Column(String) # estate or neighborhood
    type = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    floor_space_sqf = Column(Integer)
    price_per_sqf = Column(Integer)
    agent_id = Column(String, ForeignKey('agents.id'))