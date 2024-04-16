import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class BorrarCoordinador:
    def GET(self, username):
        coordinador = model.get_coordinador_by_username(username)
        return render.borrar_coordinador(coordinador=coordinador)

    def POST(self, username):
        if model.delete_coordinador(username):
            # Redirigir a la página de coordinadores después de borrar
            raise web.seeother('/coordinadores')
        else:
            return "Error al eliminar el coordinador"
