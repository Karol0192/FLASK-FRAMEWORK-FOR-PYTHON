from flask import Flask,render_template,url_for,request,redirect
import os 
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')


supabase = create_client(url,key)

app = Flask(__name__)

@app.route('/')
def index():
    data = supabase.table('cursos').select('*').order('id').execute()
    cursos = data.data
    cantidad_cursos = len(cursos)
    #print(cursos)
    return render_template('index.html',cursos=cursos,
                        cantidad_cursos=cantidad_cursos)

@app.route('/detalle/<id>')
def detalle(id):
    
    # Obtenemos los datos del curso con id = n
    data = supabase.table('cursos').select('*').eq('id',id).execute()
    curso = data.data[0]
    print(curso)

    return render_template('detalle.html',curso=curso)

@app.route('/editar/<id>',methods=['GET','POST'])
def editar(id):

    # Obtenemos los datos del registro id = n
    data = supabase.table('cursos').select('*').eq('id',id).execute()
    curso = data.data[0]

    if request.method == 'POST':
        nombre = request.form['nombre']
        instructor = request.form['instructor']
        topico = request.form['topico']

        supabase.table('cursos').update({
            'nombre':nombre,
            'instructor':instructor,
            'topico':topico
        }).eq('id',id).execute()

        return redirect(url_for('index'))
    
    return render_template('editar.html',curso=curso)

if __name__ == '__main__':
    app.run(debug=True)