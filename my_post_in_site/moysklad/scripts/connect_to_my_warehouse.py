import requests
import base64
#Коннект по токену
def ConnectByToken (token):
    # token = '93c96fb9feb98f7c5acf8fc1a18a221659d9d7e3' Нынешний токен. Передаем как аргумент к функции
    headers = {'Authorization':'Bearer ' + token,}
    return headers
#Коннект по паре логин\пароль
def ConnectByLog (logpass):
    logpass = logpass.encode('Utf-8')
    q = base64.b64encode (logpass)
    s = q.decode('UTF-8')
    headers = {'Authorization':'Basic ' + s,}
    return headers
