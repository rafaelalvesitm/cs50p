from fpdf import FPDF

border_x = 10
page_height = 297
page_width = 210

# Prompts the user for a name
name = input("Enter your name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.set_margin(0)
pdf.add_page()
pdf.set_font("Helvetica", size=60, style="B")
pdf.cell(210, 50, txt="CS50 Shirtificate", align="C", new_x="LEFT", new_y="LAST")
pdf.image("shirtificate.png", x=border_x, y=70, w=page_width - 2 * border_x)
pdf.set_font("Helvetica", size=40, style="B")
pdf.set_text_color(255, 255, 255)
pdf.cell(210, 250, txt=name, align="C")
pdf.output("shirtificate.pdf.pdf")
