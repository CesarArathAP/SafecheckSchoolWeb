from pymongo import MongoClient

class SafeCheck:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.directores_collection = self.db['directores']
        self.carreras_collection = self.db['carreras']
        self.visitas_collection = self.db['visitas']

    def get_director_by_username(self, username):
        return self.directores_collection.find_one({"username": username})

    def get_especialidades_by_carrera_id(self, carrera_id):
        carrera = self.carreras_collection.find_one({"carrera_id": carrera_id})
        if carrera:
            return carrera.get('especialidades', [])
        return []

    def get_alumnos_by_especialidad(self, especialidad_id):
        for carrera in self.carreras_collection.find():
            for especialidad in carrera['especialidades']:
                if especialidad['id'] == especialidad_id:
                    return especialidad.get('alumnos', [])
        return []

    def get_alumno_by_matricula(self, matricula):
        for carrera in self.carreras_collection.find():
            for especialidad in carrera['especialidades']:
                for alumno in especialidad['alumnos']:
                    if alumno['matricula'] == matricula:
                        return alumno
        return None

    def obtener_visitas(self):
        try:
            return list(self.visitas_collection.find())
        except Exception as e:
            print("Error al obtener las visitas:", e)
        return []