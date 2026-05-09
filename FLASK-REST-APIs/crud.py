from flask import Flask
from flask_restful import Resource,Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required
from user import User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

api = Api(app)
jwt = JWT(app,authenticate,identity)

puppies = []

#########################################################
class Puppy(db.Model):

    name = db.Column(db.String(80),primary_key=True)

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'nombre':self.name}
########################################################

class PuppyNames(Resource):

    def get(self,name):

        pup = Puppy.query.filter_by(name=name).first()

        if pup:
            return pup.json()
        else:
            return {'name':None},404
        
        """for pup in puppies:
            if pup['name'] == name:
                return pup"""
        
        ##return {'name':None}

    def post(self,name):

        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()

        #pup = {'name':name}

        #puppies.append(pup)

        #return pup

    def delete(self,name):

        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            db.session.delete(pup)
            db.session.commit()
            return {'message':'deleted'}

        return {'message':'not found'},404
        
        """for ind,pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(ind)
                print(deleted_pup)
                return {'note':'deleted success'}"""
            
class AllNames(Resource):

    #@jwt_required()
    def get(self):
        #return {'puppies':puppies}
        puppies = Puppy.query.all()
        return [pup.json() for pup in puppies]
    
api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)