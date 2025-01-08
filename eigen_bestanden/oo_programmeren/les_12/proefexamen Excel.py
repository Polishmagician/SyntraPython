from openpyxl import Workbook, load_workbook


#Definieer plek excel
bestand = "teambuilding.xlsx"

#Lees excel in
wb_start = load_workbook(bestand)
sheet_start = wb_start.active #Sheet 1

# Create a new workbook for the filter
wb_combined = Workbook()
combined_sheet = wb_combined.active
combined_sheet.title = "Activiteiten met lunch"
#Headers maken voor new workbook
headers = [cell.value for cell in sheet_start[1]]
combined_sheet.append(headers)

#List to save data to
data = []

#Toon data
for row in sheet_start.iter_rows(min_row=2, values_only=True):
    data.append(row)
