from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/projects", methods=["GET"])
def get projects():
	data = request.json
	return jsonify(f"reply from endpoint get projects, data = {data}")

@app.route("/project", methods=["GET"])
def get project():
	data = request.json
	return jsonify(f"reply from endpoint get project, data = {data}")

@app.route("/project", methods=["DELETE"])
def delete project():
	data = request.json
	return jsonify(f"reply from endpoint delete project, data = {data}")

@app.route("/project", methods=["PUT"])
def update project():
	data = request.json
	return jsonify(f"reply from endpoint update project, data = {data}")

@app.route("/project", methods=["POST"])
def create project():
	data = request.json
	return jsonify(f"reply from endpoint create project, data = {data}")

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)