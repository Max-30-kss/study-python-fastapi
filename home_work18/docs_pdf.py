from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# DOCX в PDF (простий приклад)
def docx_to_pdf(docx_file, pdf_file):
    doc = open(docx_file, 'r')  # Читання DOCX (це лише приклад, краще використовувати бібліотеку python-docx)
    lines = doc.readlines()
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    y_position = height - 40  # Початкова позиція для тексту

    for line in lines:
        c.drawString(40, y_position, line.strip())
        y_position -= 15

        if y_position < 40:
            c.showPage()
            y_position = height - 40

    c.save()
