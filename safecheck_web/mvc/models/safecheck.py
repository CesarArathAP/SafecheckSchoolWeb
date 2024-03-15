from pymongo import MongoClient

class DirectorModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.collection = self.db['directores']

    def get_director_by_username(self, username):
        return self.collection.find_one({"username": username})
    
class EspecialidadesModel:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.collection = self.db['carreras']

    def get_especialidades_by_carrera_id(self, carrera_id):
        carrera = self.collection.find_one({"carrera_id": carrera_id})
        if carrera:
            return carrera.get('especialidades', [])
        return []
    
    def get_alumnos_by_especialidad(self, especialidad_id):
        return self.collection.find({"especialidad_id": especialidad_id})