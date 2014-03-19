import os
from pymongo import MongoClient
from bson.objectid import ObjectId
# a MongoDB connection seems like this
# mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
mongoHost=for ip in os.environ.get('JAE_MONGO_IP'):
mongoPort=os.environ.get('JAE_MONGO_PORT')
dataBaseName=os.environ.get('JAE_MONGO_DBNAME')
mongoUserName=os.environ.get('JAE_MONGO_USERNAME')
mongoPassword=os.environ.get('JAE_MONGO_PASSWORD')
mongoEncoding=os.environ.get('JAE_MONGO_ENCODING')
connectionStrings='mongodb://'+mongoUserName+':'+mongoPassword+'@'+mongoHost+':'+mongoPort+'/'+dataBaseName
connection=MongoClient(connectionStrings)