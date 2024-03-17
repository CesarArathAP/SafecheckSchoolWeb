import web

render = web.template.render('mvc/views/', base="layout")

class Notifications:
    def GET(self):
        return render.notifications()