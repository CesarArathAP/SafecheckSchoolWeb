import os
import web
from mvc.models.safecheck import SafeCheck
from fpdf import FPDF

render = web.template.render('mvc/views/', base="layout")

class VerAlumno:
    def GET(self, matricula):
        model = SafeCheck()
        alumno = model.get_alumno_by_matricula(matricula)
        if alumno:
            return render.ver_alumno(alumno)
        else:
            return "Alumno no encontrado"

    def POST(self, matricula):
        model = SafeCheck()
        alumno = model.get_alumno_by_matricula(matricula)
        if alumno:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Crear contenido del PDF
            contenido = f"""
            Reporte de Alumno
            Matrícula: {alumno['matricula']}
            Nombre: {alumno['nombre']} {alumno['apellido_paterno']} {alumno['apellido_materno']}
            Correo Electrónico: {alumno['correo_electronico']}
            Grupo: {alumno['grupo']}
            NSS: {alumno['nss']}
            Estado: {alumno['estado']}
            """

            pdf.multi_cell(0, 10, contenido)

            # Definir la ruta de la carpeta donde se guardará el PDF
            carpeta_pdf = "pdf/"
            if not os.path.exists(carpeta_pdf):
                os.makedirs(carpeta_pdf)

            # Definir el nombre del archivo PDF como la matrícula del alumno
            pdf_output = f"{carpeta_pdf}{alumno['matricula']}.pdf"
            pdf.output(pdf_output)

            # Enviar el PDF al cliente para descarga
            web.header('Content-Type', 'application/pdf')
            web.header('Content-disposition', 'attachment; filename=%s' % pdf_output)
            return open(pdf_output, "rb").read()
        else:
            return "Alumno no encontrado"