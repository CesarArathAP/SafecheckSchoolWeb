
import web

render = web.template.render('mvc/views/')

class Registro:
    def GET(self):
        return render.registro()
