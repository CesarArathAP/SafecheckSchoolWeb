import web

urls = (
    '/', 'mvc.controllers.login.Login'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()