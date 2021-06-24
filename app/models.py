from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin,db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)

    applicant = db.relationship('Application',backref = 'user',lazy = "dynamic")
  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def _repr_(self):
        return f'User {self.username}'


class Courses(db.Model):
    _tablename_ = 'course'
    id = db.Column(db.Integer,primary_key = True)
    institution = db.Column(db.String(150),index =True)
    title = db.Column(db.String(255),index =True)
    description = db.Column(db.String(12255))
    
class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer,primary_key = True)
    applicant = db.Column(db.String(150),index =True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    institution = db.Column(db.String(150),index =True)
    programme = db.Column(db.String(150),index =True)
    intake = db.Column(db.String(150),index =True)
    
    
