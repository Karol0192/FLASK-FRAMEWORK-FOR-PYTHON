from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    
    name = StringField('Name of Puppy')
    submit = SubmitField('Add Puppy')



class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')