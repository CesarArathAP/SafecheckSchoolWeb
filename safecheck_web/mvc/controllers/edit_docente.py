import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class EditarDocente:
    def GET(self, id):
        try:
            # Intentar recuperar el docente por ID
            docente = model.get_docente_by_id(int(id))
            if docente:
                # Renderizar la plantilla edit_docente con los datos del docente recuperados
                return render.edit_docente(docente=docente)
            else:
                # Manejar el caso donde el docente con el ID dado no existe
                return "Docente not found"
        except ValueError:
            # Manejar el caso donde el ID proporcionado no es un entero válido
            return "Invalid ID"

    def POST(self, id):
        try:
            data = web.input()  # Obtener datos del formulario

            # Extraer datos del formulario de entrada
            nombre = data.nombre
            apellido_paterno = data.apellido_paterno
            apellido_materno = data.apellido_materno
            telefono = data.telefono
            nss = data.nss
            email = data.email
            username = data.username
            carreras_seleccionadas = [carrera.strip() for carrera in data.get('carrera', '').split('\r\n') if carrera.strip()]
            
            # Obtener las carreras asignadas al docente antes de la edición
            docente_actual = model.get_docente_by_id(int(id))
            carreras_previas = docente_actual.get('carreras', [])

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
           
            # Registrar al docente con las carreras seleccionadas o previas
            if model.update_docente(int(id), nombre, apellido_paterno, apellido_materno, telefono, nss, email, username, carreras_objects):
                # Redirigir al usuario a la página '/new' después de una actualización exitosa
                raise web.seeother('/docentes')  
            else:
                # Redirigir al usuario a la página '/error' si ocurre algún error durante la actualización
                raise web.seeother('/error')  
        except ValueError:
            # Manejar el caso donde la conversión a entero falla
            return "Invalid ID"
        except Exception as e:
            # Manejar cualquier otra excepción que pueda ocurrir durante el proceso de actualización
            return f"An error occurred: {e}"
