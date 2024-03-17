import web

render = web.template.render('mvc/views/', base="layout")

class DocenteRegistration:
    def GET(self):
        return render.docente_registration()