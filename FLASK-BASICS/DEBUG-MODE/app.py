from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Hello Puppy</h1>'

@app.route('/information')
def info():
    return f'<h1>Puppies are cute!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return f'<h1>This is a page for {name}</h1>'

@app.route('/puppy_age/<age>')
def puppy_age(age):
    return f'<h1>You are {age} old´s</h1>'

if __name__ == '__main__':
    app.run(debug=True)