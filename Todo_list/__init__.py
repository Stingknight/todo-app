from flask import Flask,redirect,render_template,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///sample.db'
app.config['SECRET_KEY']='hello'


db=SQLAlchemy(app)

from Todo_list import routes
from Todo_list import model
