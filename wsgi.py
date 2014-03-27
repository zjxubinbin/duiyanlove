#coding=utf-8
from flask import Flask,url_for,redirect,render_template,session,request
import os 

application=app=Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
	return render_template('index.htm')


@app.route('/companylist')
def companyList():
	return render_template('companylist.htm')

@app.route('/companydetails/<companyID>')
def companyDetails(companyID):
	return render_template('companyDetails.html',company=getCompanyByID(companyID))

@app.route('/members')
def allMembers():
	return render_template('membersList.htm')

@app.route('/member/<memberID>')
def memberDetails(memberID):
	return render_template('memberDetails.htm',memeber=getMemberByID(memberID))

@app.route('/myindex')
def myindex():
	if session.get('login'):
		return render_template('myindex.htm',allthings=getAllAboutMemberByID(session.get('memberID')))

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		User=getUserByUserName(request.form['userName'])
		if User['passWords']==request.form['passWords']:
			session['login']==True
		else:
			return render_template('login.htm')
	else:
		return render_template('login.htm')

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method=='POST':
		if regUser(request.form['userName'],request.form['EMail'],request.form['passWords'])!=None:
			redirect(url_for('home'))
		else:
			return render_template('register.htm')
	else:
		return render_template('register.htm')

@app.route('/publish',methods=['GET','POST'])
def publish():
	if request.method=='POST':
		# if publish:
		pass
	else:
		return render_template('publish.htm')

@app.route('/subscribe')
def subscribe():
	return render_template('subscribe.htm')


# 静态文件路由
@app.route('/static/<path:file>')
def staticFiles(file):
	return url_for('static',filename=file)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)