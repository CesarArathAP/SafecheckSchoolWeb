import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/index', 'mvc.controllers.login.Login',
    '/new', 'mvc.controllers.new_registration.NewRegistration',
    '/new/new_docente', 'mvc.controllers.docente_registration.DocenteRegistration',
    '/new/new_vigilante', 'mvc.controllers.vigilancia_registration.VigilanciaRegistration',
    '/new/new_directores', 'mvc.controllers.directores_registration.DirectoresRegistration',
    '/docente_registration', 'mvc.controllers.docente_registration.DocenteRegistration',
    '/directores_registration', 'mvc.controllers.directores_registration.DirectoresRegistration',
    '/vigilancia_registration', 'mvc.controllers.vigilancia_registration.VigilanciaRegistration',
    r'/visitas', 'mvc.controllers.visitas.Visitas',
    '/notifications', 'mvc.controllers.notifications.Notifications',
    r'/especialidades/(\d+)', 'mvc.controllers.especialidades.Especialidades',
    r'/docentes/(\d+)', 'mvc.controllers.docentes.Docentes',
    r'/alumnos/(.*)', 'mvc.controllers.lista_alumnos.ListaAlumnos',
    r'/ver_alumno/(\d+)', 'mvc.controllers.ver_alumno.VerAlumno',
    r'/ver_visita/(\d+)', 'mvc.controllers.ver_visita.VerVisita',
    r'/ver_docente/(\d+)', 'mvc.controllers.ver_docente.VerDocente',
    '/visitas/resultado', 'mvc.controllers.search_visits.SearchVisits',
    r'/editar_docente/(\d+)', 'mvc.controllers.edit_docente.EditarDocente',
    r'/actualizar_docente/(\d+)', 'mvc.controllers.edit_docente.ActualizarDocente',
    r'/borrar/(\w+)', 'mvc.controllers.borrar_docente.BorrarDocente'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()