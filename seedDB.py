import database

tasks = [
    {
        '_id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        '_id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

colls = database.db.list_collection_names()

for i in colls:
	coll = database.db[i]
	coll.drop()


database.db.tasks.insert_many(tasks)