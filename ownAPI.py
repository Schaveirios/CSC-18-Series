from flask import Flask, request, jsonify

app = Flask(__name__)


students = [{"name" : "John"}, {"name" : "Jean"}, {"name" : "Ace"}]

@app.route('/', methods=['GET'])
def index():
	return jsonify({"response" : "it works!"})

@app.route('/stud', methods=['GET'])
def allstud():
	return jsonify({'students' : students})

@app.route('/stud/<string: name>', methods =['GET'])
def returnStud(name):
	studs = [student for student in students if student['name'] == name]
	return jsonify({'student' : studs[0]})

@app.route('/stud', methods=['POST'])
def addstud():
	studs = {"name" : request.json['name']}
	students.append(studs)
	return jsonify({'students' : students})

@app.route('/stud/<string: name>', methods=['PUT'])
def editName(name):
	studs = [student for student in students if student['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'student' : students})

@app.route('/stud/<string: name>', methods = ['DELETE'])
def removeStud(name):
	studs = [student for student in students if student['name'] == name]
	students.remove(studs[0])
	return jsonify({'name': name})

	
if __name__ == "__main__":
    app.run(debug=True, port=8080)