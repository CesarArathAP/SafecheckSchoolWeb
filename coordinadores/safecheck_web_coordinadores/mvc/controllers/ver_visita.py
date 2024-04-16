import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class VerVisita:
    def GET(self, id):
        visita = model.get_visita_by_id(int(id))
        return render.ver_visita(visita=visita)