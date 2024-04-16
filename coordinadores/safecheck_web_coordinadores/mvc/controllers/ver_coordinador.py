import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class VerCoordinador:
    def GET(self, username):
        coordinador = model.get_coordinador_by_username(username)
        return render.ver_coordinador(coordinador=coordinador)
