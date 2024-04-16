import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class VerPolicias:
    def GET(self, username):
        policia = model.obtener_policia_por_username(username)
        return render.ver_policias(policia=policia)
