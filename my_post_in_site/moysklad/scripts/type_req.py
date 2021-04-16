import requests
import json
def SimplReqByUrl (url,headers):
    params = {} #{'filter=type=product','type=service','type=demand'}'meta':'product',
    response = requests.get(url, params=params, headers=headers)# params=params,
    r = response.json()
    with open("data_file.json", "w") as write_file: #Временная затычка для создания json файла
        json.dump(r, write_file)
    return [r, response]