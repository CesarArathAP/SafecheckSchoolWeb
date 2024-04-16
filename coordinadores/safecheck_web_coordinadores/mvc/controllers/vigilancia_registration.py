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

       
    # Insertar el policía en la colección de vigilancia
        if model.registrar_policia(nombre, apellidos, telefono, username, password):
                raise web.seeother('/new')  # Redirigir a una página de éxito
        else:
            print("Error al registrar policía:")
            raise web.seeother('/error')  # Redirigir a una página de error