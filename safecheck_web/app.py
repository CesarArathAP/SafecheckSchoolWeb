import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/index', 'mvc.controllers.login.Login',
    '/new', 'mvc.controllers.new_registration.NewRegistration',
    '/new/new_docente', 'mvc.controllers.docente_registration.DocenteRegistration',
    '/new/new_vigilante', 'mvc.controllers.vigilancia_registration.VigilanciaRegistration',
    '/new/new_directores', 'mvc.controllers.directores_registration.DirectoresRegistration',
    '/registros', 'mvc.controllers.registration.Registration',
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
    '/docentes', 'mvc.controllers.docentess.DocentesObtenidos',
    r'/editar_docente/(\d+)', 'mvc.controllers.edit_docente.EditarDocente',
    r'/actualizar_docente/(\d+)', 'mvc.controllers.edit_docente.ActualizarDocente',
    r'/borrar_docente/(\d+)', 'mvc.controllers.borrar_docente.BorrarDocente',
    '/coordinadores', 'mvc.controllers.coordinadores.CoordinadoresObtenidos',
    r'/editar_coordinador/(\w+)', 'mvc.controllers.edit_coordinador.EditarCoordinador',
    r'/actualizar_coordinador/(\w+)', 'mvc.controllers.edit_coordinador.EditarCoordinador',
    r'/borrar_coordinador/(\w+)', 'mvc.controllers.borrar_coordinador.BorrarCoordinador',
    r'/ver_coordinador/(\w+)', 'mvc.controllers.ver_coordinador.VerCoordinador',
    '/policias', 'mvc.controllers.policias.PoliciasObtenidos',
    r'/ver_policia/(\w+)', 'mvc.controllers.ver_policias.VerPolicias',
    r'/editar_policia/(\w+)', 'mvc.controllers.edit_policia.EditarPolicia',
    r'/actualizar_policia/(\w+)', 'mvc.controllers.edit_policia.EditarPolicia',
    r'/borrar_policia/(\w+)', 'mvc.controllers.borrar_policia.BorrarPolicia',

)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()