import web

render = web.template.render('mvc/views/', base="layout")

class VigilanciaRegistration:
    def GET(self):
        return render.vilancia_registration()