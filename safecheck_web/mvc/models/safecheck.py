from pymongo import MongoClient
import hashlib

class SafeCheckModel:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://...")  # Utiliza tu URL de conexión
        self.db = self.client.safecheck  # Nombre de tu base de datos
        self.docentes_collection = self.db.docentes  # Colección de docentes

    def verificar_credenciales(self, username, password):
        # Buscar al docente por el nombre de usuario
        docente = self.docentes_collection.find_one({"username": username})
        if docente:
            # Verificar si la contraseña coincide con el hash MD5 almacenado en la base de datos
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if docente["password"] == hashed_password:
                return True  # Credenciales correctas
        return False  # Credenciales incorrectas