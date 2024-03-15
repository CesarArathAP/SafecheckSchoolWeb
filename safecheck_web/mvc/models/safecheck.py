from pymongo import MongoClient

class DirectorModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.collection = self.db['directores']

    def get_director_by_username(self, username):
        return self.collection.find_one({"username": username})