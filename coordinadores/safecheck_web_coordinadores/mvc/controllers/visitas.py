import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class Visitas:
    def GET(self):
        model = SafeCheck()
        visitas = model.obtener_visitas()  # Obtener los datos de las visitas desde el modelo
        return render.visitas(visitas=visitas)  # Pasar los datos de las visitas a la plantilla