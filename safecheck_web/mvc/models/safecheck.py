import random
from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class SafeCheck:

    # DEFINIR LA RUTA DE LA BASE DE DATOS Y LAS COLECCIONES

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.directores_collection = self.db['directores']
        self.carreras_collection = self.db['carreras']
        self.visitas_collection = self.db['visitas']
        self.docentes_collection = self.db['docentes']
        self.vigilancia_collection = self.db['vigilancia']

    # METODO PARA INCIAR SESION COMO DIRECTOR
    def get_director_by_username(self, username):
        return self.directores_collection.find_one({"username": username})
    
    # METODO PARA OBTENER LAS ESPECIALIDADES DE LAS CARRERAS QUE TIENE ACARGO EL DIRECTOR

    def get_especialidades_by_carrera_id(self, carrera_id):
        carrera = self.carreras_collection.find_one({"carrera_id": carrera_id})
        if carrera:
            return carrera.get('especialidades', [])
        return []
    
    # METODO PARA MOSTRAR LA LISTA DE LOS ALUMNOS DE CADA ESPECIALIDAD DE CADA CARRERA

    def get_alumnos_by_especialidad(self, especialidad_id):
        for carrera in self.carreras_collection.find():
            for especialidad in carrera['especialidades']:
                if especialidad['id'] == especialidad_id:
                    return especialidad.get('alumnos', [])
        return []
    
    # METODO PARA MOSTRAR A UN ALUMNO EN LA VISTA ALUMNO

    def get_alumno_by_matricula(self, matricula):
        for carrera in self.carreras_collection.find():
            for especialidad in carrera['especialidades']:
                for alumno in especialidad['alumnos']:
                    if alumno['matricula'] == matricula:
                        return alumno
        return None
    
    # MOSTRAR LAS VIISTAS EN LA VISTA

    def obtener_visitas(self):
        try:
            visitas = list(self.visitas_collection.find())
            return visitas
        except Exception as e:
            print("Error al obtener las visitas:", e)
            return []
    # METODO PARA REGISTRAR A UN DOCENTE NUEVO Y ASIGNAR UNA O VARIAS CARRERAS
        
    def registrar_docente(self, nombre, apellido_paterno, apellido_materno, telefono, nss, correo, username, password_md5, carreras):
        # Generar un nuevo id único de dos dígitos
        new_id = self.obtener_proximo_id()
        
        # Crear el documento del docente con el nuevo id
        docente_data = {
            "id": new_id,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "telefono": telefono,
            "nss": nss,
            "email": correo,
            "username": username,
            "password_md5": password_md5,
            "carreras": carreras
        }

        try:
            self.docentes_collection.insert_one(docente_data)
            return True  # Retorna True si el registro fue exitoso
        except PyMongoError as e:
            print("Error al registrar docente:", e)
            return False  # Retorna False si ocurrió un error durante el registro

    def obtener_proximo_id(self):
        # Generar un nuevo id de dos dígitos aleatorio que no esté en uso
        while True:
            new_id = random.randint(10, 99)  # Generar un nuevo id aleatorio de dos dígitos
            if not self.docentes_collection.find_one({"id": new_id}):  # Verificar si el id ya está en uso
                return new_id
            
    # METODO PARA REGISTRAR A UN OFICIAL DE POLICIA
    def registrar_policia(self, nombre, apellidos, telefono, username, password):
        # Crear el documento del policía
        policia_data = {
            "nombre": nombre,
            "apellidos": apellidos,
            "telefono": telefono,
            "username": username,
            "password": password
        }
        try:
            self.vigilancia_collection.insert_one(policia_data)
            return True  # Retorna True si el registro fue exitoso
        except PyMongoError as e:
            print("Error al registrar policía:", e)
            return False  # Retorna False si ocurrió un error durante el registro

    # METODO PARA OBTENER A LOS DOCNETES POR CARRERA
    def obtener_docentes_por_carrera(self, carrera_id):
        # Filtrar los docentes que tienen el carrera_id proporcionado
        return self.docentes_collection.aggregate([
            {"$match": {"carreras.id": carrera_id}},
            {"$project": {"_id": 1, "id": 1, "nombre": 1, "apellido_paterno": 1, "apellido_materno": 1, "telefono": 1, "nss": 1, "email": 1, "username": 1, "password_md5": 1}}
        ])
    
    # METODO PARA VER VISITA EN UNA VISTA
    def get_visita_by_id(self, id):
        return self.visitas_collection.find_one({'id': id})