from flask import Flask,render_template,url_for,redirect,session,flash
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):

    breed = StringField('What breed are you?',
                        validators=[DataRequired()])
    
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data
        flash(f'You just changed your bread to: {breed}','success')

        return redirect(url_for('index'))

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)