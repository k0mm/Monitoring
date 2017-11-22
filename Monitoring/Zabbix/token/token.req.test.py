import requests
import base64
import urllib3
from sys import argv
#Отсекаем всякие предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


api = 'https://api.dating.com/identity'

usrPass = "test@nyxale.ru:132132131"
# usrPass = "20244066431:132132131"


b64Val = (base64.b64encode(bytes(usrPass, 'utf-8'))).decode("utf-8")
r = requests.get(api,verify=False, headers={"Authorization": "Basic %s" % b64Val})
print(r)
print(r.headers['X-Token'])
print(r.text)







# Проверяем на валидность
a = 'api.dating.com'
b = '20244066431'
c = r.headers['X-Token']





url = "https://"+ a +'/credits/accounts/'+ b +"/balance"
token = "Token token="+'"'+c+'"'
headers={}
print(token)
headers['authorization'] = token
print(headers)
response = requests.get(url,verify=False,headers=headers)
js = response #.text()
# js=js.get('balance')
print(js)
