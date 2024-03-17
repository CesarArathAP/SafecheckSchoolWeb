import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class Especialidades:
    def GET(self, carrera_id):
        model = SafeCheck()
        especialidades = model.get_especialidades_by_carrera_id(int(carrera_id))
        return render.especialidades(especialidades=especialidades)