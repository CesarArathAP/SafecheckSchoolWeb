from pymongo import MongoClient

class SafeCheck:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['safecheckschool']
        self.directores_collection = self.db['directores']
        self.carreras_collection = self.db['carreras']
        self.visitas_collection = self.db['visitas']
        self.docentes_collection = self.db['docentes']
        self.policias_collection = self.db['policias']

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
            visitas = list(self.visitas_collection.find())
            return visitas
        except Exception as e:
            print("Error al obtener las visitas:", e)
        return[]

    def registrar_docente(self, nombre, apellido1, apellido2, correo, contrasena, num_trabajador, carreras):
        docente_data = {
            "nombre": nombre,
            "apellido_paterno": apellido1,
            "apellido_materno": apellido2,
            "correo": correo,
            "contrasena": contrasena,
            "num_trabajador": num_trabajador,
            "carreras": []  # Inicializar lista de carreras
        }

        # Agregar las carreras seleccionadas al documento del docente
        for carrera in carreras:
            carrera_data = self.obtener_datos_carrera(carrera['id'])  # Obtener datos de la carrera por su ID
            if carrera_data:
                docente_data['carreras'].append({"id": carrera['id'], "nombre": carrera_data['nombre']})

        try:
            self.docentes_collection.insert_one(docente_data)
            return True  # Retorna True si el registro fue exitoso
        except Exception as e:
            print("Error al registrar docente:", e)
        return False  # Retorna False si ocurrió un error durante el registro

    def registrar_policia(self, nombre, apellidos, telefono, username, password):
        policia_data = {
             "nombre": nombre,
             "apellidos": apellidos,
             "telefono": telefono,
             "username": username,
            "password": password
         }

        try:
            self.policias_collection.insert_one(policia_data)
            return True  # Retorna True si el registro fue exitoso
        except Exception as e:
            print("Error al registrar policía:", e)
        return False  # Retorna False si ocurrió un error durante el registro

