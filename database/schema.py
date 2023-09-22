from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()





Base = db.Model
relationship = db.relationship
Column = db.Column
Integer = db.Integer
String = db.String
Boolean = db.Boolean
DateTime = db.DateTime
Numeric = db.Numeric
ForeignKey = db.ForeignKey
Sequence = db.Sequence
db_session = db.session

class User(Base):
    __tablename__= 'users'

    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=True)
    admin = Column(Boolean)