from flask import Flask
from flask_cors import CORS
from crud_mysql import crud
from mysql_database import Database, DatabaseCreds
import os, logging

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(crud)

if __name__ == "__main__":
	db = Database("project", DatabaseCreds(os.getenv("DATABASE_HOST"), os.getenv("DATABASE_USER"), os.getenv("DATABASE_PASSWORD")))
	app.run(host="0.0.0.0", debug=True, port=5000)