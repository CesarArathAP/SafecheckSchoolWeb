import web
from mvc.models.safecheck import SafeCheck
import hashlib

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class DirectoresRegistration:
    def GET(self):
        return render.directores_registration()
    
    def POST(self):
        form = web.input()
        username = form.username
        email = form.email
        password_md5 = hashlib.md5(form.password_md5.encode()).hexdigest()  # Convertir la contraseña a MD5
        nss = form.nss
        numero_trabajador = form.numero_trabajador
        telefono = form.telefono
        nombre = form.nombre
        apellido_paterno = form.apellido_paterno
        apellido_materno = form.apellido_materno
        
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

        

        # Insertar los datos en la base de datos
        if model.registrar_coordinador(username, email, password_md5, nss, numero_trabajador, telefono, nombre, apellido_paterno, apellido_materno, carreras_objects):
            raise web.seeother('/new')  # Redirigir a una página de éxito
        else:
            error_message = "Hubo un error al registrar al director. Por favor, inténtalo de nuevo más tarde."
            raise web.seeother('/error?message=' + error_message)
