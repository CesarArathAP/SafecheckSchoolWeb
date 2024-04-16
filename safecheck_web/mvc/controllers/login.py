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
        user, user_type = model.login(username, password)

        if user_type == "admin":
            # Si el usuario es un administrador, redirigir al usuario a la vista de administrador
            return render.index(administrador=user)  # Pasar el administrador como un parámetro
        elif user_type == "director":
            # Si el usuario es un director, redirigir al usuario a la vista de director
            return render.index(director=user)  # Pasar el director como un parámetro
        else:
            # Si no se encontró el usuario o la contraseña es incorrecta, mostrar mensaje de error
            return render.password_incorrect()
