import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class BorrarCoordinador:
    
        def GET(self, id):
            coordinador = model.get_coordinador_by_id(int(id))
            return render.borrar_coordinador(coordinador=coordinador)
    
        def POST(self, id):
            model.delete_coordinador(int(id))
            # Redirigir a la página de coordinadores después de borrar
            raise web.seeother('/new')  # Redirige a la página de coordinadores después de borrar