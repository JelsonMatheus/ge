from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.tables import Table, TableStyle, colors
from django.http import FileResponse
import io


def factory_paragraph(text, fontSize, *args, **kwargs):
    pstyle = ParagraphStyle(
        name='p', fontSize=fontSize, *args, **kwargs
    )
    return Paragraph(text, style=pstyle)


def factory_table(data, *args, **kwargs):
    table = Table(data, *args, **kwargs)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                              ('FONTSIZE', (0, 0), (0, -1), 10),
                              ('FONTSIZE', (1, 0), (-1, -1), 10),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('GRID', (0, 0), (-1, -1), 0.25, colors.black)]))
    return table


def report_turma(turmas):
    buffer = io.BytesIO()
    elements = []
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm)
    doc.title = "Turmas"

    table = factory_table(turmas, rowHeights=0.5*cm, repeatRows=1)
    title = factory_paragraph('Relatório de Turmas', fontSize=18, alignment=1)

    elements.extend([title, Spacer(1, 1*cm)])
    elements.append(table)
    doc.build(elements)
    buffer.seek(io.SEEK_SET)
    response = FileResponse(buffer, as_attachment=False, filename='turma.pdf')
    return response


def report_servidor(servidores):
    buffer = io.BytesIO()
    elements = []
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm)

    table = factory_table(servidores, repeatRows=1)
    title = factory_paragraph('Relatório de Servidores', fontSize=18, alignment=1)

    elements.extend([title, Spacer(1, 1*cm)])
    elements.append(table)
    doc.build(elements)
    buffer.seek(io.SEEK_SET)
    response = FileResponse(buffer, as_attachment=False, filename='servidor.pdf')
    return response


def report_aluno(matriculas):
    buffer = io.BytesIO()
    elements = []
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm)

    table = factory_table(matriculas, repeatRows=1)
    title = factory_paragraph('Relatório de Alunos', fontSize=18, alignment=1)

    elements.extend([title, Spacer(1, 1*cm)])
    elements.append(table)
    doc.build(elements)
    buffer.seek(io.SEEK_SET)
    response = FileResponse(buffer, as_attachment=False, filename='aluno.pdf')
    return response


    
def report_matricula(matriculas):
    buffer = io.BytesIO()
    elements = []
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm)

    table = factory_table(matriculas, repeatRows=1)
    title = factory_paragraph('Relatório de Matrículas', fontSize=18, alignment=1)

    elements.extend([title, Spacer(1, 1*cm)])
    elements.append(table)
    doc.build(elements)
    buffer.seek(io.SEEK_SET)
    response = FileResponse(buffer, as_attachment=False, filename='matricula.pdf')
    return response

