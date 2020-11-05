from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
import models
import os
from utils import get_data, get_filters

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
# 'mysql://username:password@server/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'designforgreen.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/greendesign'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)



# two decorators, same function
@app.route('/')
# @app.route('/index.html',methods=['GET'])
def index():
  userlist = ['Bangalore', 'Delhi', 'Chennai']
  deplist=['Bangalore', 'Delhi', 'Chennai']
  intercomlist=['Bangalore', 'Delhi', 'Chennai']
  communelist=['Bangalore', 'Delhi', 'Chennai']
  referencelist=['Bangalore', 'Delhi', 'Chennai']
  donnes_infralist=['Bangalore', 'Delhi', 'Chennai']
  intercomlist=[['Bangalore'], ['Delhi'], ['Chennai']]
  mapbox_access_token = 'pk.eyJ1Ijoidm5pc2hhbnQxMDEyIiwiYSI6ImNraDRpazVhZTA2aGkzNWswZWYxd2F2MGcifQ.Mf3OEq6F9oZ1xTY_IKNpWQ'
  req=get_filters()
  data=get_data()
  return render_template('index.html',mapbox_access_token=mapbox_access_token,req=req,data=data)

@app.route('/index_get_data',methods=['POST'])
def stuff():
  # Assume data comes from somewhere else
  print("Hello from stuff")
  filters=request.get_json()
  print(filters)
  data = {
    "data": get_data(filters)
  }
  print(data)
  mapbox_access_token = 'pk.eyJ1Ijoidm5pc2hhbnQxMDEyIiwiYSI6ImNraDRpazVhZTA2aGkzNWswZWYxd2F2MGcifQ.Mf3OEq6F9oZ1xTY_IKNpWQ'
  
  return jsonify(data)
  #return render_template('index.html',mapbox_access_token=mapbox_access_token,req=data)


@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
