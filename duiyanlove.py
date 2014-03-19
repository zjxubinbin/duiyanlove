from flask import Flask,route,url_for,redirect,render_template
from mongoModels.mongoModels import *
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return connectionStrings