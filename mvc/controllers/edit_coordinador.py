import web
from mvc.models.safecheck import SafeCheck


render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class EditarCoordinador:
    def GET(self, id):
        try:
            coordinador = model.get_coordinador_by_id(int(id))
            if coordinador:
                return render.edit_coordinador(coordinador=coordinador)
            else:
                return "Coordinador not found"
        except ValueError:
            return "Invalid ID"
        
    def POST(self, id):
        try:
            data = web.input()
            
            nombre = data.nombre
            apellido_paterno = data.apellido_paterno
            apellido_materno = data.apellido_materno
            telefono = data.telefono
            nss = data.nss
            email = data.email
            username = data.username
            password_md5 = data.password_md5
            carreras_seleccionadas = [carrera.strip() for carrera in data.get('carrera', '').split('\r\n') if carrera.strip()]
            
            coordinador_actual = model.get_coordinador_by_id(int(id))
            carreras_previas = coordinador_actual.get('carreras', [])
            
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
            
            if carreras_seleccionadas:
                carreras_objects = [{"id": carreras_disponibles[carrera], "nombre": carrera} for carrera in carreras_seleccionadas]
            else:
                carreras_objects = [{"id": carrera['id'], "nombre": carrera['nombre']} for carrera in carreras_previas]
                
            model.edit_coordinador(int(id), nombre, apellido_paterno, apellido_materno, telefono, nss, email, username, password_md5, carreras_objects)
            return "Coordinador updated successfully"
        except ValueError:
            return "Invalid ID"
        