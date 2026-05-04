from flask import Flask,render_template,url_for,redirect
from forms import AddForm,DelForm
from extensions import db,Migrate
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ===============================================================
# DATABASE CONFIG
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ===============================================================

# ===============================================================

db.init_app(app)

from models import Puppy,Owner

Migrate(app,db)

# VIEWS 
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/list',methods=['GET'])
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/add',methods=['GET','POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_new = Puppy(name)
        db.session.add(puppy_new)
        db.session.commit()

        return redirect(url_for('list_pup'))
        
    return render_template('add.html',form=form)

@app.route('/delete',methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        puppy_id = form.id.data

        # Asegurarnos de que exista
        puppy = db.session.get(Puppy,puppy_id)

        if puppy is not None:
            db.session.delete(puppy)
            db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html',form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)


