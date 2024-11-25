from data_gerechten import *
import random as rd
from tabulate import tabulate

#Gerechten omzetten in menu's

dag_menu_1 = {"voorgerecht": rd.choice(voorgerechten),
              "hoofdgerecht": rd.choice(hoofdgerechten),
              "dessert": rd.choice(desserts)}
dag_menu_2 = {"voorgerecht": rd.choice(voorgerechten),
              "hoofdgerecht": rd.choice(hoofdgerechten),
              "dessert": rd.choice(desserts)}
dag_menu_3 = {"voorgerecht": rd.choice(voorgerechten),
              "hoofdgerecht": rd.choice(hoofdgerechten),
              "dessert": rd.choice(desserts)}

menus = [dag_menu_1,dag_menu_2,dag_menu_3]


#Alles in lijsten gieten voor visualisatie
headers = ["Dagmenu 1","Dagmenu 2","Dagmenu 3"]
voorgerecht = ["Voorgerecht",dag_menu_1['voorgerecht'],dag_menu_2['voorgerecht'],dag_menu_3['voorgerecht']]
hoofdgerecht = ["Hoofdgerecht",dag_menu_1['hoofdgerecht'],dag_menu_2['hoofdgerecht'],dag_menu_3['hoofdgerecht']]
dessert = ["Dessert",dag_menu_1['dessert'],dag_menu_2['dessert'],dag_menu_3['dessert']]

vis_data = [voorgerecht,hoofdgerecht,dessert]
# print(tabulate(vis_data, headers=headers))