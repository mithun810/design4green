from routes import db


class data_indexed(db.Model):
    __tablename__ = 'data_indexed'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    Commune= db.Column(db.Text)
    Department= db.Column(db.Text)
    intercommunalite= db.Column(db.Text)
    region= db.Column(db.Text)
    population= db.Column(db.Float)
    score_global_department= db.Column(db.Float)
    score_global_intercommunalite= db.Column(db.Float)
    score_global_region= db.Column(db.Float)
    donnes_infra_communales= db.Column(db.Text)
    code_iris= db.Column(db.Integer)
    Commune_id= db.Column(db.Integer)
    Department_id= db.Column(db.Integer)
    intercommunalite_id= db.Column(db.Integer)
    region_id= db.Column(db.Integer)
    nom_iris= db.Column(db.Text)
    access_al_information_department= db.Column(db.Float)
    access_al_information_intercommunalite= db.Column(db.Float)
    access_al_information_region= db.Column(db.Float)
    access_aux_interfaces_numeriques_departement= db.Column(db.Float)
    access_aux_interfaces_numeriques_intercommunalite= db.Column(db.Float)
    access_aux_interfaces_numeriques_region= db.Column(db.Float)
    competences_administative_department= db.Column(db.Float)
    competences_administative_intercommunalite= db.Column(db.Float)
    competences_administative_region= db.Column(db.Float)
    competence_numeriques_department= db.Column(db.Float)
    competence_numeriques_intercommunalite= db.Column(db.Float)
    competence_numeriques_region= db.Column(db.Float)
    global_access_department= db.Column(db.Float)
    global_access_intercommunalite= db.Column(db.Float)
    global_access_region= db.Column(db.Float)
    global_competence_department= db.Column(db.Float)
    global_competence_intercommunalite= db.Column(db.Float)
    global_competence_region= db.Column(db.Float)
    geo_points= db.Column(db.Text)


class School(db.Model):
    __tablename__ = 'School'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True) 
    LOC_CODE = db.Column(db.Text)