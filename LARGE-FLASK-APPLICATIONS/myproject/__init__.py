from flask import Flask
from dotenv import load_dotenv
from myproject.extensions import db,migrate
import os 

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey10121'

# BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app,db)


from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprints

app.register_blueprint(owners_blueprints,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')



