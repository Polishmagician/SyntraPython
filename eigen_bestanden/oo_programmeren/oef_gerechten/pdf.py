# Import classes and data
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import *

def create_tables():
    #Data te halen uit main
    tables = {}
    for index,menu in enumerate(menus):
        voorgerecht = ["Voorgerecht",menu['voorgerecht']]
        hoofdgerecht = ['Hoofdgerecht',menu['hoofdgerecht']]
        dessert = ['Dessert',menu['dessert']]
        data = [voorgerecht,hoofdgerecht,dessert]
        table = tabulate(data)
        tables[f"Dagmenu {index+1}"] = table
    return tables

# Functie om PDF te genereren
def generate_pdf(filename="dagmenu.pdf"):
    # Maak een canvas object
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Startpositie
    y_position = height - 40  # Begin bovenaan de pagina

    # Itereer over de dagmenu's in de dictionary
    dagmenu_dict = create_tables()
    for menu, content in dagmenu_dict.items():
        # Schrijf de titel
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y_position, menu)
        y_position -= 20

        # Schrijf de inhoud
        c.setFont("Helvetica", 10)
        for line in content.split("\n"):
            if y_position < 40:  # Maak een nieuwe pagina als we onderaan komen
                c.showPage()
                c.setFont("Helvetica", 10)
                y_position = height - 40

            c.drawString(40, y_position, line)
            y_position -= 15

        # Voeg extra ruimte tussen de menu's
        y_position -= 20

    # Sla de PDF op
    c.save()

# Genereer de PDF
generate_pdf()
