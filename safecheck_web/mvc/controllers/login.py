import web

render = web.template.render('mvc/views/', base="layout")

class Login:
    def GET(self):
        return render.login()