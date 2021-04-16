import xlwt
#Импортируем наш файл с функцией авторизации
import scripts.connect_to_my_warehouse
#Обработка ответа
import scripts.type_req
#Экспорт в эксель
import scripts.export
#Используем модуль авторизации по токену. В качестве аргумента передаем строку в которой содержится токен
#headers = connect_to_my_warehouse.ConnectByToken('93c96fb9feb98f7c5acf8fc1a18a221659d9d7e3') # по токену
logpass = 'admin@rvb801:qwerty5483148' # Ligin\Password
headers = scripts.connect_to_my_warehouse.ConnectByLog(logpass)#По паре логин пароль
result = scripts.type_req.SimplReqByUrl('https://online.moysklad.ru/api/remap/1.2/report/stock/all', headers)
data = result[0]['rows']
scripts.export.ExportInExcel(data)
