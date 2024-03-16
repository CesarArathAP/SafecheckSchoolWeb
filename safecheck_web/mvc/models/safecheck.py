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
        # Busca una especialidad por su id
        especialidad = self.collection.find_one({"especialidades.id": especialidad_id})
        if especialidad:
            # Encuentra la lista de alumnos dentro de la especialidad
            for esp in especialidad['especialidades']:
                if esp['id'] == especialidad_id:
                    return esp.get('alumnos', [])
        return []