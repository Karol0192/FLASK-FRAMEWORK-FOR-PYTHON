from flask import Flask,render_template,request,redirect,session
from supabase import create_client
from dotenv import load_dotenv
import os 


load_dotenv()

app = Flask(__name__)
app.secret_key = 'secret1234'

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase = create_client(url,key)

@app.route('/')
def index():

    data = supabase.table('producto').select('*').execute()

    productos = data.data

    return render_template(
        'index.html',
        productos=productos)

@app.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        try:

            response = supabase.auth.sign_in_with_password({
                'email':email,
                'password':password
            })
        
            session['user'] = response.user.email

            return redirect('/')
        
        except Exception as e:
            return str(e)
        
    return render_template('login.html')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

