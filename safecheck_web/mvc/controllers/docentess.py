import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class DocentesObtenidos:
    def GET(self):
        model = SafeCheck()
        docentes = model.obtener_docentess()  # Obtener los datos de las visitas desde el modelo
        return render.docentes(docentes=docentes)  # Cambiado de coordinador a coordinadores
  # Pasar los datos de las visitas a la plantilla