from flask import Flask, jsonify, abort, make_response, request
from bson.json_util import dumps
import database

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	return dumps(database.db.tasks.find())

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	task = database.db.tasks.find_one({'_id' : task_id})
	if not task:
		abort(404)
	return jsonify(task)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = {
		'_id' : database.tasks.count_documents({}) + 1,
		'title' : request.json['title'],
		'description': request.json.get('description', ""),
		'done': False
	}
	database.tasks.insert_one(task)
	return jsonify(task), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	task = database.db.tasks.find_one({'_id' : task_id})
	if not task:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != str:
		abort(400)
	if 'description' in request.json and type(request.json['description']) != str:
		abort(400)
	if 'done' in request.json and type(request.json['done']) != bool:
		abort(400)
	database.tasks.update_one({'_id' : task_id}, { '$set' : request.json})
	return request.json

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	task = database.db.tasks.find_one({'_id' : task_id})
	if not task:
		abort(404)
	database.tasks.delete_one({'_id' : task_id})
	return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)