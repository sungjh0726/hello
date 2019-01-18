import openpyxl

book = openpyxl.load_workbook("./melon_top_100.xlsx")
sheet = book.worksheets[0]

data = []
for r in sheet.rows:
    data.append([ r[0].value, r[1].value, r[3].value ])

del data[0]    # header 제거

data = sorted(data, key=lambda x: x[2], reverse=True)

