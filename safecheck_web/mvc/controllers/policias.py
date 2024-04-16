import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class PoliciasObtenidos:
    def GET(self):
        model = SafeCheck()
        policias = model.obtener_policias()  # Obtener los datos de las visitas desde el modelo
        return render.policias(policias=policias)  # Cambiado de coordinador a coordinadores
  # Pasar los datos de las visitas a la plantilla