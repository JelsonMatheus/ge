from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table,TableStyle,colors
from django.http import FileResponse
import io



def report_turma(turmas):
  buffer = io.BytesIO()
  elements = []
  doc = SimpleDocTemplate(buffer, pagesize=A4)
  c_width=[1.8*inch]
  table = Table(turmas,rowHeights=30,repeatRows=1,colWidths=c_width)

  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                            ('FONTSIZE',(0,0),(-1,-1),9),
                            ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                            ('GRID', (0,0), (-1,-1), 0.25, colors.black)]))

  elements.append(table)
  doc.build(elements)
  buffer.seek(io.SEEK_SET)
  response = FileResponse(buffer, as_attachment=False, filename='turma.pdf')
  return response

def report_servidor(servidores):
  buffer = io.BytesIO()
  elements = []
  doc = SimpleDocTemplate(buffer, pagesize=A4)
  c_width=[1.2*inch,1*inch,1*inch,0.8*inch,1.8*inch]
  table = Table(servidores,rowHeights=30,repeatRows=1,colWidths=c_width)

  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                            ('FONTSIZE',(0,0),(-1,-1),9),
                            ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                            ('GRID', (0,0), (-1,-1), 0.25, colors.black)]))

  elements.append(table)
  doc.build(elements)
  buffer.seek(io.SEEK_SET)
  response = FileResponse(buffer, as_attachment=False, filename='servidor.pdf')
  return response

def report_aluno(alunos):
  buffer = io.BytesIO()
  elements = []
  doc = SimpleDocTemplate(buffer, pagesize=A4)
  c_width=[1*inch]
  table = Table(alunos,rowHeights=30,repeatRows=1,colWidths=c_width)

  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                            ('FONTSIZE',(0,0),(-1,-1),9),
                            ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                            ('GRID', (0,0), (-1,-1), 0.25, colors.black)]))

  elements.append(table)
  doc.build(elements)
  buffer.seek(io.SEEK_SET)
  response = FileResponse(buffer, as_attachment=False, filename='aluno.pdf')
  return response
