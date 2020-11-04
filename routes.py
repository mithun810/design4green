from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import models
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'designforgreen.db')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)



# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    print("Total number of schools is", models.School.query.count())
    return render_template('index.html')

@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else
  data = {
    "data": [
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      },
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      },
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      },
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      },
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      },
      {
        "Nom Com": "1",
        "Code Iris": "John Q Public",
        "Rank of ScoreGlobal": "System Architect",
        "Nom Iris": "$320,800",
        "Population": "2011/04/25",
        "Score Global": "Edinburgh",
        "Acces Aux_interfaces_numeriques_intercommunalite": "5421",
        "Access Al_information_intercommunalite": "1",
        "competences_administative_intercommunalite": "John Q Public",
        "competence_numeriques_intercommunalite": "System Architect",
        "global_access_intercommunalite": "$320,800",
        "global_competence_intercommunalite": "2011/04/25"
      }]
  }
  return jsonify(data)

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
