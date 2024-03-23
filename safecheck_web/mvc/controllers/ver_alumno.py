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
            motivo = web.input().motivo  # Obtener el motivo del reporte del formulario
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Logo en la parte izquierda
            pdf.image('C:/Users/miguel angel/Documents/SafecheckSchoolWeb-main/safecheck_web/static/images/logo.png', x=10, y=10, w=33)
            # Logo en la parte derecha
            pdf.image('C:/Users/miguel angel/Documents/SafecheckSchoolWeb-main/safecheck_web/static/images/logo.png', x=170, y=10, w=33)

            # Crear contenido del PDF con formato mejorado
            pdf.set_font("Arial", style='B', size=16)
            pdf.cell(200, 10, txt="Reporte de Alumno", ln=True, align='C')
            pdf.set_font("Arial", style='', size=12)
            pdf.ln(10)  # Salto de línea

            pdf.ln(5)
            # Detalles del alumno
            pdf.cell(0, 10, f"Matrícula: {alumno['matricula']}", ln=True)
            pdf.cell(0, 10, f"Nombre: {alumno['nombre']} {alumno['apellido_paterno']} {alumno['apellido_materno']}", ln=True)
            pdf.cell(0, 10, f"Correo Electrónico: {alumno['correo_electronico']}", ln=True)
            pdf.cell(0, 10, f"Grupo: {alumno['grupo']}", ln=True)
            pdf.cell(0, 10, f"NSS: {alumno['nss']}", ln=True)
            pdf.cell(0, 10, f"Estado: {alumno['estado']}", ln=True)
            pdf.ln(10)  # Salto de línea

            # Motivo del reporte
            pdf.cell(200, 10, txt="Motivo del Reporte:", ln=True, align='L')
            pdf.multi_cell(0, 10, txt=motivo)

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
