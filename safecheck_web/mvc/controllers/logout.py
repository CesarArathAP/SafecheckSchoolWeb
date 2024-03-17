# logout.py
import web

class Logout:
    def GET(self):
        raise web.seeother('/')