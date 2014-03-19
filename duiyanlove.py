from flask import Flask,url_for,redirect,render_template,session,request
import os 

app=Flask(__name__)

mongoHost=os.environ.get('JAE_MONGO_IP')
mongoPort=os.environ.get('JAE_MONGO_PORT')
dataBaseName=os.environ.get('JAE_MONGO_DBNAME')
mongoUserName=os.environ.get('JAE_MONGO_USERNAME')
mongoPassword=os.environ.get('JAE_MONGO_PASSWORD')
mongoEncoding=os.environ.get('JAE_MONGO_ENCODING')

mongodbInfo=[mongoHost,mongoPort,dataBaseName,mongoUserName,mongoPassword,mongoEncoding]
@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html',mongodbInfo=mongodbInfo)
	

if __name__=='__main__':
	app.run(host="0.0.0.0",port=80,debug=True)