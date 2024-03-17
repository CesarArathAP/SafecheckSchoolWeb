import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base="layout")

class VerAlumno:
    def GET(self, matricula):
        model = SafeCheck()
        alumno = model.get_alumno_by_matricula(matricula)
        if alumno:
            return render.ver_alumno(alumno)
        else:
            return "Alumno no encontrado"