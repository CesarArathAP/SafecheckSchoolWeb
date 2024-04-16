import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class BorrarPolicia:
    def GET(self, username):
        # Mostrar una página de confirmación antes de borrar al policía
        policia = model.obtener_policia_por_username(username)
        return render.borrar_policia(policia=policia)

    def POST(self, username):
        # Eliminar al policía
        success = model.eliminar_policia(username)
        if success:
            # Redirigir al usuario a la página de policias después de la eliminación
            raise web.seeother('/policias')
        else:
            # Manejar el caso de eliminación fallida
            return "Error al eliminar el policía"
