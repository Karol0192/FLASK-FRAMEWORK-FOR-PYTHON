from sqlalchemy import (Integer,Text,
                        Column,ForeignKey)
from extensions import db

class Puppy(db.Model):

    __tablename__ = 'puppies'
    
    id = Column(Integer,primary_key=True)
    name = Column(Text)

    owner = db.relationship(
        'Owner',
        backref='puppy',
        uselist=False,
        cascade='all,delete-orphan'
    )

    def __init__(self,name):
        self.name = name

class Owner(db.Model):

    __tablename__ = 'owners'

    id = Column(Integer,primary_key=True)
    name = Column(Text)

    puppy_id = Column(Integer,ForeignKey(
        'puppies.id'),
        unique=True)
    
    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    