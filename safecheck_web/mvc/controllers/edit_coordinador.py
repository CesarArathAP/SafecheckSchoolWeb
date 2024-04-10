import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class EditarCoordinador:
    def GET(self, username):
        try:
            # Intentar recuperar el coordinador por su nombre de usuario
            coordinador = model.get_coordinador_by_username(username)
            if coordinador:
                # Renderizar la plantilla edit_coordinador con los datos del coordinador recuperados
                return render.edit_coordinador(coordinador=coordinador)
            else:
                # Manejar el caso donde el coordinador con el nombre de usuario dado no existe
                return "Coordinador not found"
        except Exception as e:
            # Manejar cualquier otra excepción que pueda ocurrir durante la recuperación del coordinador
            return f"An error occurred: {e}"

    def POST(self, username):
        try:
            data = web.input()  # Obtener datos del formulario

            # Extraer datos del formulario de entrada
            nombre = data.nombre
            apellido_paterno = data.apellido_paterno
            apellido_materno = data.apellido_materno
            telefono = data.telefono
            nss = data.nss
            email = data.email
            carreras_seleccionadas = [carrera.strip() for carrera in data.get('carrera', '').split('\r\n') if carrera.strip()]
            
            # Obtener las carreras asignadas al coordinador antes de la edición
            coordinador_actual = model.get_coordinador_by_username(username)
            carreras_previas = coordinador_actual.get('carreras', [])

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
            
            # Obtener los IDs de las carreras seleccionadas o mantener las previas si no hay selecciones nuevas
            if carreras_seleccionadas:
                carreras_objects = [{"id": carreras_disponibles[carrera], "nombre": carrera} for carrera in carreras_seleccionadas]
            else:
                carreras_objects = carreras_previas
           
            # Actualizar al coordinador con las carreras seleccionadas o previas
            if model.update_coordinador(username, nombre, apellido_paterno, apellido_materno, telefono, nss, email, carreras_objects):
                # Redirigir al usuario a la página '/new' después de una actualización exitosa
                raise web.seeother('/coordinadores')  
            else:
                # Redirigir al usuario a la página '/error' si ocurre algún error durante la actualización
                raise web.seeother('/error')  
        except Exception as e:
            # Manejar cualquier otra excepción que pueda ocurrir durante el proceso de actualización
            return f"An error occurred: {e}"


    