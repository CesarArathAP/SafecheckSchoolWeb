import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class ListaAlumnos:
    def GET(self, especialidad_id):
        try:
            especialidad_id = float(especialidad_id)
            model = SafeCheck()
            alumnos = model.get_alumnos_by_especialidad(especialidad_id)
            return render.lista_alumnos(alumnos=alumnos)
        except ValueError:
            return "Especialidad ID inválido"