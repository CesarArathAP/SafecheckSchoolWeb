import web
from mvc.models.safecheck import EspecialidadesModel

render = web.template.render('mvc/views/', base="layout")

class ListaAlumnos:
    def GET(self, especialidad_id):
        model = EspecialidadesModel()
        alumnos = model.get_alumnos_by_especialidad(especialidad_id)
        return render.lista_alumnos(alumnos=alumnos)