from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,Text
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#####################################################
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(Integer,primary_key=True)
    name = db.Column(Text)
    age = db.Column(Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} year/s old'
    







