from flask import Flask

app = Flask(__name__)

# if a puppy name does not end in a y add on a y to the name
# if a puppy name does end in a y, replace it with iful instead

@app.route('/')
def index():
    return f'<h1>Welcome! Go to/puppy_latin/name to see your name in puppy latin!</h1>'

@app.route('/puppy_latin/<name>')
def puppy_latin(name:str):
    
    if name.endswith('y'):
        name = name[:-1] + 'iful'
    else:
        name = name + 'y'
    
    return f'<h1>Hi Rufus! Your puppylatin name is {name.capitalize()}</h1>'



if __name__ == '__main__':
    app.run(debug=True)