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
        apellido_paterno = form.apellido_paterno
        apellido_materno = form.apellido_materno
        telefono = form.telefono
        nss = form.nss
        email = form.email
        username = form.username
        password_md5 = form.password_md5
        # Obtener carreras y dividirlas en una lista
        carreras = [carrera.strip() for carrera in form.get('carrera', '').split('\r\n') if carrera.strip()]
        # Formatear carreras como lista de objetos
        carreras_objects = [{"nombre": carrera} for carrera in carreras]
       
        if model.registrar_docente(nombre, apellido_paterno, apellido_materno, telefono, nss, email, username, password_md5, carreras_objects):
            raise web.seeother('/new')  
        else:
            raise web.seeother('/error')