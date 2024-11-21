from c_gerecht import *

data = [
    # Voorgerechten
    {"naam": "Tomatensoep", "omschrijving": "Een rijke, romige tomatensoep met verse basilicum.", "prijs": 5.95, "soort_gerecht": "voorgerecht"},
    {"naam": "Caesarsalade", "omschrijving": "Een klassieke salade met romaine sla, croutons, Parmezaanse kaas en Caesarsaus.", "prijs": 7.50, "soort_gerecht": "voorgerecht"},
    {"naam": "Bruschetta", "omschrijving": "Gegrild brood met tomaat, basilicum en olijfolie.", "prijs": 6.00, "soort_gerecht": "voorgerecht"},
    {"naam": "Carpaccio", "omschrijving": "Dun gesneden ossenhaas met rucola, Parmezaanse kaas en truffelmayonaise.", "prijs": 9.50, "soort_gerecht": "voorgerecht"},
    {"naam": "Garnalencocktail", "omschrijving": "Klassieke cocktail met Hollandse garnalen en whisky-cocktailsaus.", "prijs": 10.25, "soort_gerecht": "voorgerecht"},
    {"naam": "Franse uiensoep", "omschrijving": "Traditionele soep met gekarameliseerde uien en een krokante kaascrouton.", "prijs": 6.75, "soort_gerecht": "voorgerecht"},
    {"naam": "Caprese salade", "omschrijving": "Mozzarella, tomaat en verse basilicum met een drizzle van balsamico.", "prijs": 7.95, "soort_gerecht": "voorgerecht"},
    {"naam": "Loempia", "omschrijving": "Kleine knapperige loempia gevuld met groenten en kip.", "prijs": 5.25, "soort_gerecht": "voorgerecht"},
    {"naam": "Vitello Tonnato", "omschrijving": "Dun gesneden kalfsvlees met tonijnmayonaise en kappertjes.", "prijs": 10.95, "soort_gerecht": "voorgerecht"},
    {"naam": "Geitenkaas salade", "omschrijving": "Salade met warme geitenkaas, walnoten en honing.", "prijs": 8.50, "soort_gerecht": "voorgerecht"},

    # Hoofdgerechten
    {"naam": "Ribeye steak", "omschrijving": "Perfect gegrilde ribeye steak geserveerd met gegrilde groenten en aardappelpuree.", "prijs": 22.95, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Vegetarische lasagne", "omschrijving": "Een heerlijke lasagne met verse groenten, bechamelsaus en tomatensaus.", "prijs": 18.75, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Kip Tandoori", "omschrijving": "Malse kip gemarineerd in tandoorikruiden met rijst en naanbrood.", "prijs": 19.95, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Zalmfilet", "omschrijving": "Gegrilde zalm met citroen-botersaus en seizoensgroenten.", "prijs": 21.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Spaghetti Bolognese", "omschrijving": "Traditionele Italiaanse pasta met gehaktsaus en Parmezaanse kaas.", "prijs": 16.25, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Schnitzel", "omschrijving": "Krokant gebakken schnitzel met citroen en frietjes.", "prijs": 17.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Risotto met paddenstoelen", "omschrijving": "Romige risotto met een mix van wilde paddenstoelen en Parmezaan.", "prijs": 19.95, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Mixed Grill", "omschrijving": "Een selectie van gegrild vlees geserveerd met knoflooksaus en groenten.", "prijs": 24.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Vegetarische curry", "omschrijving": "Een kruidige curry met kokosmelk, groenten en basmatirijst.", "prijs": 18.00, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Hamburger Deluxe", "omschrijving": "Huisgemaakte hamburger met cheddar, bacon en friet.", "prijs": 16.95, "soort_gerecht": "hoofdgerecht"},

    # Desserts
    {"naam": "Chocolade mousse", "omschrijving": "Luchtige chocolade mousse, geserveerd met een vleugje slagroom.", "prijs": 6.50, "soort_gerecht": "dessert"},
    {"naam": "Tiramisu", "omschrijving": "Italiaanse klassieker met mascarpone, koffie en een vleugje cacao.", "prijs": 7.25, "soort_gerecht": "dessert"},
    {"naam": "Crème brûlée", "omschrijving": "Een klassiek Frans dessert met een krokante gekarameliseerde suikerlaag.", "prijs": 6.75, "soort_gerecht": "dessert"},
    {"naam": "Dame Blanche", "omschrijving": "Vanille-ijs met warme chocoladesaus en slagroom.", "prijs": 5.95, "soort_gerecht": "dessert"},
    {"naam": "Cheesecake", "omschrijving": "Romige cheesecake met een bodem van speculaas.", "prijs": 6.50, "soort_gerecht": "dessert"},
    {"naam": "Appeltaart", "omschrijving": "Huisgemaakte appeltaart met kaneel en een bolletje vanille-ijs.", "prijs": 5.50, "soort_gerecht": "dessert"},
    {"naam": "Sorbet", "omschrijving": "Verfrissende sorbet met vers fruit en bessen.", "prijs": 6.25, "soort_gerecht": "dessert"},
    {"naam": "Panna Cotta", "omschrijving": "Italiaans dessert met vanille en een topping van rood fruit.", "prijs": 6.95, "soort_gerecht": "dessert"},
    {"naam": "Mango-ijs", "omschrijving": "Romig mango-ijs met een vleugje limoen.", "prijs": 5.75, "soort_gerecht": "dessert"},
    {"naam": "Chocoladetaart", "omschrijving": "Rijke chocoladetaart met een zachte kern.", "prijs": 7.95, "soort_gerecht": "dessert"},

    # Extra gerechten voor volledigheid
    {"naam": "Biefstuk", "omschrijving": "Malse biefstuk geserveerd met champignonroomsaus.", "prijs": 23.95, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Lamsrack", "omschrijving": "Gegrilde lamsrack met rozemarijnsaus en aardappelgratin.", "prijs": 27.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Pizza Margherita", "omschrijving": "Traditionele pizza met tomaat, mozzarella en basilicum.", "prijs": 12.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Pasta Carbonara", "omschrijving": "Romige pasta met spekjes en Parmezaanse kaas.", "prijs": 14.95, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Gepocheerde peer", "omschrijving": "Gepocheerde peer met rode wijnsaus en vanille-ijs.", "prijs": 7.00, "soort_gerecht": "dessert"},
    {"naam": "Gegrilde groentesalade", "omschrijving": "Salade met gegrilde paprika, courgette en feta.", "prijs": 8.25, "soort_gerecht": "voorgerecht"},
    {"naam": "Eendeborst", "omschrijving": "Gebakken eendeborst met sinaasappelsaus en aardappelrozet.", "prijs": 25.50, "soort_gerecht": "hoofdgerecht"},
    {"naam": "Minestrone soep", "omschrijving": "Italiaanse groentesoep met een vleugje pesto.", "prijs": 6.50, "soort_gerecht": "voorgerecht"}
]

#Data omzetten in class gerechten
voorgerechten = []
hoofdgerechten = []
desserts = []

for g in data:
    if g['soort_gerecht'] == 'voorgerecht':
        new_gerecht = gerecht(g['naam'], g['omschrijving'], g['prijs'], g['soort_gerecht'])
        voorgerechten.append(new_gerecht)
    elif g['soort_gerecht'] == 'hoofdgerecht':
        new_gerecht = gerecht(g['naam'], g['omschrijving'], g['prijs'], g['soort_gerecht'])
        hoofdgerechten.append(new_gerecht)
    else:
        new_gerecht = gerecht(g['naam'], g['omschrijving'], g['prijs'], g['soort_gerecht'])
        desserts.append(new_gerecht)
