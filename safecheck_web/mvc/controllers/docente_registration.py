import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class DocenteRegistration:
    def GET(self):
        return render.docente_registration()
    
    def POST(self):
        form = web.input()
        nombre = form.nombre
        apellido1 = form.apellido1
        apellido2 = form.apellido2
        correo = form.correo
        contrasena = form.contrasena
        num_trabajador = form.num_trabajador
        carreras = []  # Inicializar lista de carreras

        # Obtener las carreras seleccionadas
        for key, value in form.items():
            if key.startswith('carrera_'):
                carreras.append(value)

        # Intenta registrar al docente en la base de datos
        if model.registrar_docente(nombre, apellido1, apellido2, correo, contrasena, num_trabajador, carreras):
            # Si el registro fue exitoso, redirige a alguna página de éxito
            raise web.seeother('/new')  # Cambia '/exito' por la URL que desees
        else:
            # Si ocurrió un error, muestra un mensaje de error o redirige a alguna página de error
            raise web.seeother('/error')  # Cambia '/error' por la URL que desees