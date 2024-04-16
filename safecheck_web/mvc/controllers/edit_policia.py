import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")
model = SafeCheck()

class EditarPolicia:
    def GET(self, username):
        policia = model.obtener_policia_por_username(username)
        return render.edit_policia(policia=policia)

    def POST(self, username):
        data = web.input()
        # Actualizar el policía, excluyendo la contraseña
        success = model.actualizar_policia(
            username, 
            data.nombre, 
            data.apellidos, 
            data.telefono, 
            data.username  # Agregamos el nombre de usuario para la actualización
        )
        if success:
            # Redirigir al usuario a la página de policias después de la actualización
            raise web.seeother('/policias')
        else:
            # Manejar el caso de actualización fallida
            return "Error al actualizar el policía"
