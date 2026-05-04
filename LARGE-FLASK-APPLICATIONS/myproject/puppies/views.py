from flask import Blueprint,render_template,redirect,url_for
from myproject.extensions import db 
from myproject.puppies.forms import AddForm,DelForm
from myproject.models import Puppy

puppies_blueprint = Blueprint('puppies',
                            __name__,
                            template_folder='templates/puppies')



@puppies_blueprint.route('/list',methods=['GET'])
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_new = Puppy(name)
        db.session.add(puppy_new)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
        
    return render_template('add.html',form=form)

@puppies_blueprint.route('/delete',methods=['GET','POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        puppy_id = form.id.data

        # Asegurarnos de que exista
        puppy = db.session.get(Puppy,puppy_id)

        if puppy is not None:
            db.session.delete(puppy)
            db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('delete.html',form=form)