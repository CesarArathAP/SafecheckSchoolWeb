import web

render = web.template.render('mvc/views/', base="layout")

class Registration:
    def GET(self):
        return render.registration()