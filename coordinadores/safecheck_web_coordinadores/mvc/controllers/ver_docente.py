import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class VerDocente:
    def GET(self, id):
        docente = model.get_docente_by_id(int(id))
        return render.ver_docente(docente=docente)
