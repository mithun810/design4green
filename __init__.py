from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import models
import os
from utils import get_data, get_filters
import constants

# basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
# 'mysql://username:password@server/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'designforgreen.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'+constants.db_config['password']+'@localhost:3306/'+constants.db_config['dbname']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)



# two decorators, same function
@app.route('/')
# @app.route('/index.html')
def index():
  userlist = ['Bangalore', 'Delhi', 'Chennai']
  deplist=['Bangalore', 'Delhi', 'Chennai']
  intercomlist=['Bangalore', 'Delhi', 'Chennai']
  communelist=['Bangalore', 'Delhi', 'Chennai']
  referencelist=['Bangalore', 'Delhi', 'Chennai']
  donnes_infralist=['Bangalore', 'Delhi', 'Chennai']
  intercomlist=[['Bangalore'], ['Delhi'], ['Chennai']]
  mapbox_access_token = 'pk.eyJ1Ijoidm5pc2hhbnQxMDEyIiwiYSI6ImNraDNoYmIyNzBhZTcycnF5ZTRmamttNmEifQ.0f6AIvvxNgBhNX_zvbhIBw'
  req=get_filters()
  data=get_data()
  return render_template('index.html',mapbox_access_token=mapbox_access_token,req=req,data=data)

@app.route('/index_get_data',methods=['POST'])
def stuff():
  # Assume data comes from somewhere else
  filters=request.get_json()
  data = {
    "data": get_data(filters)
  }
  return jsonify(data)


@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run()