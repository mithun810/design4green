from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import models
import os
from utils import get_data, get_filters
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
# 'mysql://username:password@server/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'designforgreen.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sqlpassword@localhost:3306/designforgreen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    data=get_data()
    filters=get_filters()
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
