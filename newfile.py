from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import session


app=Flask(__name__)
app.debug=True

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

class profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(20),unique=False,nullable=False)
    last_name=db.Column(db.String(20),unique=False,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"Name: {self.first_name}, Age:{self.age}"

class contactinfo(db.Model):
    Mob=db.Column(db.Integer,primary_key=True)
    address=db.Column(db.String(50),unique=False,nullable=False)
    PINcode=db.Column(db.Integer)
    def __repr__(self):
        return f"self.Mob, self.address, self.PINcode"     

class tripdetails(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    destination=db.Column(db.String(15),unique=False,nullable=False)
    days=db.Column(db.Integer,primary_key=False)
    Expenses=db.Column(db.Integer,primary_key=False)
    def __repr__(self):
        return f"self.id,self.destination,self.days,self.Expenses"

class dept_info(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(20),unique=False,nullable=False,foreign_key=True)
    dept_name=db.Column(db.String(10),unique=False,nullable=False)
    def __repr__(self):
        return f"self.first_name,self.id,self.dept_name"





if __name__=="__main__":
    app.run()