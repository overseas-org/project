from flask import Flask
from flask_cors import CORS
from crud_mysql import crud
from mysql_database import Database, DatabaseCreds
import os, logging

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(crud)

if __name__ == "__main__":
	try:
		db = Database("project", DatabaseCreds(os.environ("DATABASE_HOST"), os.environ("DATABASE_USER"), os.environ("DATABASE_PASSWORD")))
		if not db:
			logging.info("db connected")
		else:
			logging.error("no db found")
	except:
		logging.error("failed to connect")
	app.run(host="0.0.0.0", debug=True, port=5000)