import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views', base="layout")
model = SafeCheck()

class Docentes:
    def GET(self, carrera_id):
        # Obtener los docentes asociados a la carrera con el ID proporcionado
        docentes = model.obtener_docentes_por_carrera(int(carrera_id))  # Convertir a entero
        print("Docentes encontrados:", docentes)  # Para depuración
        return render.docentes(docentes=docentes)