import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/login', 'mvc.controllers.login.Login',
    r'/especialidades/(\d+)', 'mvc.controllers.especialidades.Especialidades',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()