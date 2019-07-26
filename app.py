from flask import Flask, jsonify, abort, make_response
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

# @app.route('/todo/api/v1.0/tasks', methods=['POST'])
# def create_task():
# 	if not request.json or not 'title' in request.json:
# 		abort(400)
# 	task = {
# 		'_id' : # get highest id in db and add 1,
# 		'title' : request.json['title'],
# 	}


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)