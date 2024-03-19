import web
from mvc.models.safecheck import SafeCheck

render = web.template.render('mvc/views/', base='layout')

class SearchVisits:
    def GET(self):
        try:
            params = web.input()
            fecha = params.get('fecha', '')  # Fecha de búsqueda

            # Si no se proporciona ninguna fecha, mostrar todas las visitas
            if not fecha:
                model = SafeCheck()
                visitas = model.obtener_visitas()  # Obtener todas las visitas
            else:
                # Realizar la búsqueda de visitas por fecha
                model = SafeCheck()
                visitas = model.buscar_vistas_por_fecha(fecha)

            # Renderizar la vista con los resultados de la búsqueda
            return render.resultados_busqueda(resultados=visitas)
        except Exception as e:
            return f"Error al buscar visitas: {str(e)}"