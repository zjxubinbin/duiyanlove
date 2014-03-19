import os

mongoHost=os.environ.get('JAE_MONGO_IP')
mongoPort=os.environ.get('JAE_MONGO_PORT')
dataBaseName=os.environ.get('JAE_MONGO_DBNAME')
mongoUserName=os.environ.get('JAE_MONGO_USERNAME')
mongoPassword=os.environ.get('JAE_MONGO_PASSWORD')
mongoEncoding=os.environ.get('JAE_MONGO_ENCODING')