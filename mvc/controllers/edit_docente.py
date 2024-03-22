import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class EditarDocente:
    def GET(self, id):
        docente = model.get_docente_by_id(int(id))
        return render.edit_docente(docente=docente)
