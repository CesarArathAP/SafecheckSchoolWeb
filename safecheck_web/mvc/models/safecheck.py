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
    def registrar_docente(self, nombre, apellido1, apellido2, telefono, nss, correo, username, contrasena, carreras):
        docente_data = {
            "nombre": nombre,
            "apellido_paterno": apellido1,
            "apellido_materno": apellido2,
            "telefono": telefono,
            "nss": nss,
            "email": correo,
            "username": username,
            "password_md5": contrasena,
            "carreras": carreras
        }

        try:
            self.docentes_collection.insert_one(docente_data)
            return True  # Retorna True si el registro fue exitoso
        except PyMongoError as e:
            print("Error al registrar docente:", e)
            return False  # Retorna False si ocurrió un error durante el registro
    # METODO PARA REGISTRAR A UN OFICIAL DE POLICIA