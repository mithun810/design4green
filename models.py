from routes import db

class School(db.Model):
    __tablename__ = 'School'
    __table_args__ = { 'extend_existing': True }
    LOC_CODE = db.Column(db.Text, primary_key=True) 