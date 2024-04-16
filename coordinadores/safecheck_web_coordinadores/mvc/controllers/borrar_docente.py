import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class BorrarDocente:

    def GET(self, id):
        docente = model.get_docente_by_id(int(id))
        return render.borrar_docente(docente=docente)

    def POST(self, id):
        model.delete_docente(int(id))
        # Redirigir a la página de docentes después de borrar
        raise web.seeother('/new')  # Redirige a la página de docentes después de borrar
