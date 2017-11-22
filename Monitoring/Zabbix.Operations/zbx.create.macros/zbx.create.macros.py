# Создание макроса по заданным параметрам
# -*- coding: utf-8 -*-

from pyzabbix import ZabbixAPI

# Zabbix connect
zbxurl = 'http://monitoring'
zbxname = '***********'
zbxpass = '***********'

try:
    zapi = ZabbixAPI(zbxurl)
    zapi.login(zbxname, zbxpass)
    print('Удалось подключиться к серверу Zabbix')
except Exception:
    print('Не удалось подключиться к серверу Zabbix')

#Перемнные
dataFile = "C:\p.yu\Monitoring\Zabbix.Operations\zbx.create.macros\macrosData.txt"
exthostid = 13604


#Создание максроса
def zbx_macro_crate (exthostid, extmacro, extmacrovalue):
    #print(exthostid, extmacro, extmacrovalue)
    zapi.usermacro.create(hostid = exthostid, macro = extmacro, value = extmacrovalue)
    print('Создан макрос')
#Получение списка макросов
def zbx_macro_get (hostid):
    list = []
    result = zapi.usermacro.get(hostids=hostid)  #, search={'macro': 'CP.CR'})
    for res in result:
        a=res['macro']+' - '+res['value']
        list.append(a)
    return list
#читаем файл
def read_file_to_list(dataFile):
    newValues = []
    for line in open(dataFile):
        line = line.split('\t')
        a = line[0] + ' - ' + line[1]
        newValues.append(a.rstrip())
    return newValues


newValues = read_file_to_list(dataFile)
oldValues = zbx_macro_get(exthostid)
# print(oldValues)
result=list(set(newValues) & set(oldValues))
print(result)
if not result:
    for line in open(dataFile):
        line = line.split('\t')
        #print(exthostid,"-", line[0],"-", line[1].rstrip())
        zbx_macro_crate(exthostid, line[0], line[1].rstrip())
else:
    print('\n','Ошибка!!! Есть совпадающие макросы!!!','\n','\n')
    print(result)
