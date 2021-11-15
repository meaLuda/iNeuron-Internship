from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! Test run ok "



@app.route('/user/<name>')
def user(name):
    return render_template('home.html', name=name)

    
"""
#Tell the terminal what application to run
export FLASK_APP=main.py
#Tell the terminal what application to run for windows
set FLASK_APP=main.py
#Run the application
flask run
"""