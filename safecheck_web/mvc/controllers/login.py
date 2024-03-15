# mvc/controllers/login.py

import web
from pymongo import MongoClient

render = web.template.render('mvc/views/', base="layout")

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        form = web.input()
        username = form.username
        password = form.password

        try:
            client = MongoClient('mongodb://localhost:27017/')
            db = client['safecheckschool']
            collection = db['directores']
            director = collection.find_one({"username": username, "password_md5": password})
            
            if director:
                # Director encontrado, iniciar sesión
                return "Bienvenido {}".format(director["nombre"])
            else:
                # Director no encontrado, mostrar mensaje de error
                return "Nombre de usuario o contraseña incorrectos."
        except Exception as e:
            return "Error: {}".format(e)