from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 
from dotenv import load_dotenv
from sqlalchemy import Integer,Text,ForeignKey,Column


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ====================================================
db = SQLAlchemy(app)

Migrate(app,db)
# ====================================================
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(Integer,primary_key=True)
    name = db.Column(Text)

    # Puppy to Many Toys...
    toys = db.relationship(
        'Toy',
        backref='puppy',
        lazy=True)
    
    # One Puppy --- One OWNER
    owner = db.relationship(
        'Owner',
        backref='puppy',
        uselist=False
    )

    def __init__(self,name):
        self.name = name 

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} and owner is {self.owner.name}'
        else:
            return f'Puppy name is {self.name} and has no owner yet'
    
    def report_toys(self):
        print('Here are my toys:')
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    
    __tablename__ = 'toys'

    id = Column(Integer,primary_key=True)
    item_name = Column(Text)

    puppy_id = Column(Integer,ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):
    
    __tablename__ = 'owners'

    id = Column(Integer,primary_key=True)
    name = Column(Text)

    puppy_id = Column(Integer,ForeignKey('puppies.id'),unique=True)

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
