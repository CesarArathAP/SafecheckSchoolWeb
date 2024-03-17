import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class VigilanciaRegistration:
    def GET(self):
        return render.vigilancia_registration()

    def POST(self):
        form = web.input()
        nombre = form.nombre
        apellidos = form.apellidos
        telefono = form.telefono
        username = form.username
        password = form.password

        # Intenta registrar al personal de vigilancia en la base de datos
        if model.registrar_policia(nombre, apellidos, telefono, username, password):
            # Si el registro fue exitoso, redirige a alguna página de éxito
            raise web.seeother('/new')  # Cambia '/exito' por la URL que desees
        else:
            # Si ocurrió un error, muestra un mensaje de error o redirige a alguna página de error
            raise web.seeother('/error')  # Cambia '/error' por la URL que desees
