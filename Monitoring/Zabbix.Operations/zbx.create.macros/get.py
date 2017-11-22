from pyzabbix import ZabbixAPI

# Zabbix connect
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'

try:
    zapi = ZabbixAPI(zbxurl)
    zapi.login(zbxname, zbxpass)
    print('Удалось подключиться к серверу Zabbix')
except Exception:
    print('Не удалось подключиться к серверу Zabbix')

def get_key(dict , value):
    for k, v in dict.items():
        if v == value:
            return k

def read_file_to_dict(dataFile):
    valuesDict = {}
    for line in open(dataFile):
        key, value = line.split('\t')
        # value = value.rstrip
        valuesDict[key] = value.rstrip()
    return valuesDict


dataFile = "C:\p.yu\Monitoring\Zabbix.Operations\zbx.create.macros\macrosData.txt"
a = read_file_to_dict(dataFile)


group = zapi.host.get( hostids = 13604 , output=['itemid', 'name'])
for host in group:
    items = zapi.item.get(hostids=host['hostid'],output=['itemid', 'name' ,'key_'])
    for item in items:
        itemid = item['itemid']
        print(item)
