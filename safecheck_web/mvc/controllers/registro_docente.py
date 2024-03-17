import web

render = web.template.render('mvc/views/', base="layout")

class RegistroDocente:
    def GET(self):
        # Aquí puedes manejar la lógica para mostrar el formulario de registro de docentes
        return render.registro_docente()

    def POST(self):
        # Aquí manejas el formulario de registro de docentes
        pass
