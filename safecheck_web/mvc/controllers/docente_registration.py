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
        
        # Obtener carreras seleccionadas
        carreras_seleccionadas = [carrera.strip() for carrera in form.get('carrera', '').split('\r\n') if carrera.strip()]
        
        # Lista predefinida de carreras con sus IDs
        carreras_disponibles = {
            "Diseño Digital": 1,
            "Energías Renovables": 2,
            "Industrial": 3,
            "Mecatrónica": 4,
            "Nanotecnología": 5,
            "TIC": 6,
            "Criminalística": 7,
            "Contaduría": 8,
            "Desarrollo de Negocios": 9,
            "Terapia Física": 10,
            "Lic. Enfermería": 11,
            "Lic. Salud Reproductiva": 12
        }
        
        # Obtener los IDs de las carreras seleccionadas
        carreras_objects = [{"id": carreras_disponibles[carrera], "nombre": carrera} for carrera in carreras_seleccionadas]
       
        if model.registrar_docente(nombre, apellido_paterno, apellido_materno, telefono, nss, email, username, password_md5, carreras_objects):
            raise web.seeother('/new')  
        else:
            raise web.seeother('/error')
