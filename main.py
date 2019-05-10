from flask import Flask, request, redirect
import cgi
import os
import jinja2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:8889/databaseName'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name

tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request == 'POST'
        task = request.form['TASK']
        tasks.append(task)
        
    return render_template('todos.html', title="Get it Done!", tasks=tasks)

if __name__ == '__main__':
app.run()