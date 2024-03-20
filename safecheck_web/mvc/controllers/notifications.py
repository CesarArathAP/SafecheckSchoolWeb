import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class Notifications:
    def GET(self):
        model = SafeCheck()
        reportes = model.obtener_reportes()  # Obtener los datos de las visitas desde el modelo
        return render.notifications(reportes=reportes)  # Pasar los datos de las visitas a la plantilla
