import web
from mvc.models.safecheck import SafeCheck

class BorrarDocente:
    def __init__(self, render):
        self.render = render
        self.model = SafeCheck()

    def GET(self, docente_id):
        try:
            # Eliminar el docente de la base de datos
            if self.model.eliminar_docente(docente_id):
                return web.seeother('/index')  # Redirige a la página de lista de docentes
            else:
                return self.render.error("Error al eliminar el docente.")
        except Exception as e:
            return self.render.error(str(e))

