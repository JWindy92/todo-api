# Todo-API
### A very simple API for a todo application

### Usage
* `git clone https://github.com/JWindy92/todo-api.git`
* `cd todo-api`
* `python -m venv env`
* `pip install -r requirements.txt`
* `flask run`

### Endpoints
**Get all tasks:** [GET] /todo/api/v1.0/tasks

**Get specific task:** [GET] /todo/api/v1.0/tasks/<int:task_id>

**Add new task:** [POST] /todo/api/v1.0/tasks

**Update a task:** [PUT] /todo/api/v1.0/tasks/<int:task_id>

**Delete a task:** [DELETE] /todo/api/v1.0/tasks/<int:task_id>
