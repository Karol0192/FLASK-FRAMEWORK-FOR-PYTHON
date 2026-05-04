from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Integer,Text
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#####################################################
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(Integer,primary_key=True)
    name = db.Column(Text)
    age = db.Column(Integer)
    breed = db.Column(Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} year/s old'
    