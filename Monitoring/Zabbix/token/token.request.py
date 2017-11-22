#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Получение токена для авторизации
import requests
import base64
import urllib3
from sys import argv
# Отсекаем всякие предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api = 'https://' + argv[1] + '/identity'
# api = 'https://api.dating.com/identity'
email = argv[2]
password = argv[3]

usrPass = email+':'+password
usrPass = "test@nyxale.ru:132132131"
print(usrPass)
b64Val = (base64.b64encode(bytes(usrPass, 'utf-8'))).decode("utf-8")
r = requests.get(api, verify=False,
                 headers={"Authorization": "Basic %s" % b64Val})
print(r.headers['X-Token'])
