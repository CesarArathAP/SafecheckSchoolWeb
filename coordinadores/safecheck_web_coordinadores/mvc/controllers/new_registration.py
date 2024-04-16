import web

render = web.template.render('mvc/views/', base="layout")

class NewRegistration:
    def GET(self):
        return render.new_registration()