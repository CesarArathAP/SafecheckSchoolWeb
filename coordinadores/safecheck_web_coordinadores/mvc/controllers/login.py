import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        form = web.input()
        username = form.username
        password = form.password

        model = SafeCheck()
        director = model.get_director_by_username(username)

        if director and director['password_md5'] == password:
            # Director encontrado y contraseña correcta, redirigir al usuario a la vista index
            return render.index(director=director)  # Pasar el director como un parámetro nombrado
        else:
            # Director no encontrado o contraseña incorrecta, mostrar mensaje de error
            return render.password_incorrect()