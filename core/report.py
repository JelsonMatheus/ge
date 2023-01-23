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
  table = Table(turmas, [2*inch, 2*inch])
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
  table = Table(servidores,rowHeights=35,repeatRows=1,colWidths=c_width)
  # table.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
  #                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
  #                       ('VALIGN',(0,0),(0,-1),'TOP'),
  #                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
  #                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
  #                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
  #                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
  #                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
  #                       ('GRID', (0,0), (-1,-1), 0.25, colors.black),
  #                       ]))
  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                            ('FONTSIZE',(0,0),(-1,-1),9),
                            ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                            ('GRID', (0,0), (-1,-1), 0.25, colors.black)]))

  elements.append(table)
  doc.build(elements)
  buffer.seek(io.SEEK_SET)
  response = FileResponse(buffer, as_attachment=False, filename='servidor.pdf')
  return response
