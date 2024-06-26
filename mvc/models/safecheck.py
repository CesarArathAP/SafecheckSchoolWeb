import datetime
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
        self.reportes_collection = self.db['reportes']

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
        
    # BUSCAR VISTAS POR FECHA
        
    def buscar_vistas_por_fecha(self, fecha):
        try:
            # Consultar la base de datos para las visitas en la fecha especificada
            visitas = list(self.visitas_collection.find({
                "visita.registro.fecha": fecha
            }))
            return visitas
        except Exception as e:
            print("Error al buscar las visitas por fecha:", e)
            return []
        
        #metodo para registrar a un coordinador.
    def registrar_coordinador(self, username, email, password_md5, nss, numero_trabajador, telefono, nombre, apellido_paterno, apellido_materno, carreras):
    # Generar un nuevo id único de dos dígitos
        new_id = self.obtener_proximo_id()
    
    # Crear el documento del coordinador con el nuevo id
        coordinador_data = {
            "id": new_id,
            "username": username,
            "email": email,
            "password_md5": password_md5,
            "nss": nss,
            "numero_trabajador": numero_trabajador,
            "telefono": telefono,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "carreras": carreras
    }

        try:
            self.directores_collection.insert_one(coordinador_data)
            return True  # Retorna True si el registro fue exitoso
        except PyMongoError as e:
            print("Error al registrar Coordinador:", e)
            return False   # Retorna False si ocurrió un error durante el registro

        
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
    

    # METODO PARA VER docentes EN UNA docente
    def get_docente_by_id(self, id):
        return self.docentes_collection.find_one({'id': id})
   
   

    def obtener_visitas(self):
        try:
            visitas = list(self.visitas_collection.find())
            return visitas
        except Exception as e:
            print("Error al obtener las visitas:", e)
        return[]
    
    def obtener_reportes(self):
        try:
            reportes = list(self.reportes_collection.find())
            return reportes
        except Exception as e:
            print("Error al obtener los reportes:", e)
        return []
    

    def eliminar_docente(self, docente_id):
        try:
        # Convertir el ID de string a ObjectId
            docente_id = ObjectId(docente_id)
        
        # Buscar y eliminar el docente de la colección
            result = self.docentes_collection.delete_one({"_id": docente_id})
        
            if result.deleted_count == 1:
                return True  # Retorna True si se eliminó correctamente
            else:
                return False  # Retorna False si no se encontró el docente para eliminar
        except Exception as e:
            print("Error al eliminar docente:", e)
            return False  # Retorna False si ocurrió algún error durante la eliminación
        
    def get_docente_by_id(self, id):
     return self.docentes_collection.find_one({'id': id})
