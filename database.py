from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['todoDB']
tasks = db['tasks']



if __name__ == "__main__":
    
    print(db.tasks.find_one({'_id' : 3}))
    # print(tasks.count_documents({}))