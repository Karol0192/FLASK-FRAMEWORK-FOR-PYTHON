import os 
from dotenv import load_dotenv
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

load_dotenv()
######################################################
from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


blueprint = make_google_blueprint(
                                client_id=os.getenv('client_id'),
                                client_secret=os.getenv('client_secret'),
                                offline=True,
                                scope=['profile','email'])


app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html',google=google)

@app.route('/welcome')
def welcome():
    #Verificar si el usuario esta autenticado
    if not google.authorized:
        return redirect(url_for('google.login'))
    # RETURN ERROR INTERNAL SERVER ERROR IF NOT LEGGED IN!
    resp = google.get('/oauth2/v2/userinfo')
    if not resp.ok:
        return 'Error al obtener datos del usuario',500
    
    data = resp.json()
    
    email = data['email']
    name = data.get('name')
    picture = data.get('picture')
    
    return render_template('welcome.html',
                        email=email,
                        name=name,
                        picture=picture,
                        google=google)
    
if __name__ == '__main__':
    app.run(debug=True)