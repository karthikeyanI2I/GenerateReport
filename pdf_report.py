from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak, Table, TableStyle


def pdf_write_output(data, pdf_nme, header_name=None):
    try:
        # Create a new PDF document with ReportLab
        doc = SimpleDocTemplate(pdf_nme, pagesize=letter, rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)

        MyTable = []
        for row in data:
            MyTable.append(row)

        MyData = []
        header_name = header_name.center(80)
        MyData.append(Paragraph(header_name))

        # Apply the style to the table
        MyData.append(Table(MyTable,
                            style=[('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                   ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('FONTSIZE', (0, 0), (-1, 0), 14),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                                   ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                                   ('FONTSIZE', (0, 1), (-1, -1), 12),
                                   ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)
                                   ]))
        doc.build(MyData)
    except Exception as ex:
        print(ex)

