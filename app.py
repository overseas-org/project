from flask import Flask
from flask_cors import CORS
from crud_mysql import crud

app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(crud)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=5002)