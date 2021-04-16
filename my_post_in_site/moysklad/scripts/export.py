import xlwt
def ExportInExcel (data):
    MyExcelFile = xlwt.Workbook()
    sheet = MyExcelFile.add_sheet('Имя_листа',cell_overwrite_ok=True)
    sheet.write (0,0,'Наименование товара')
    sheet.write (0,1,'Остаток')
    sheet.write (0,2,'Код')
    sheet.write (0,3,'Единицы измерения')
    row = 1
    for i in data:
        #sheet.write (row, 0, i['name'])
        sheet.write (row, 1, i['stock'])
        sheet.write (row, 2, i['code'])
        sheet.write (row, 3, i['uom']['name'])
        row += 1
    MyExcelFile.save('ExportInExcel.xls')