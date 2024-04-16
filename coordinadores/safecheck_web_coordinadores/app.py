import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/index', 'mvc.controllers.login.Login',
    r'/visitas', 'mvc.controllers.visitas.Visitas',
    '/notifications', 'mvc.controllers.notifications.Notifications',
    r'/especialidades/(\d+)', 'mvc.controllers.especialidades.Especialidades',
    r'/docentes/(\d+)', 'mvc.controllers.docentes.Docentes',
    r'/alumnos/(.*)', 'mvc.controllers.lista_alumnos.ListaAlumnos',
    r'/ver_alumno/(\d+)', 'mvc.controllers.ver_alumno.VerAlumno',
    r'/ver_visita/(\d+)', 'mvc.controllers.ver_visita.VerVisita',
    r'/ver_docente/(\d+)', 'mvc.controllers.ver_docente.VerDocente',
    '/visitas/resultado', 'mvc.controllers.search_visits.SearchVisits',
    r'/ver_coordinador/(\w+)', 'mvc.controllers.ver_coordinador.VerCoordinador'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()