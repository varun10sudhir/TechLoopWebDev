from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')