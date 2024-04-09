import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class CoordinadoresObtenidos:
    def GET(self):
        model = SafeCheck()
        coordinador = model.obtener_coordinadores()  # Obtener los datos de las visitas desde el modelo
        return render.coordinadores(coordinadores=coordinador)  # Cambiado de coordinador a coordinadores
  # Pasar los datos de las visitas a la plantilla