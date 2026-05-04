from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report',methods=['GET','POST'])
def report():
    
    username = request.form.get('username')

    if not username:
        return render_template('report.html',
                           secure=False,
                           caseNumber=False,
                           caseUpper=False,
                           caseLower=False)

    caseNumber = username[-1].isdecimal()
    caseUpper = any(letter.isupper() for letter in username)
    caseLower = any(letter.islower() for letter in username)

    secure = caseNumber and caseUpper and caseLower

    return render_template('report.html',
                           secure=secure,
                           caseNumber=caseNumber,
                           caseUpper=caseUpper,
                           caseLower=caseLower)


if __name__ == '__main__':
    app.run(debug=True)


