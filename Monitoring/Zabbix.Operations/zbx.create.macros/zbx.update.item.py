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

# Указать путь к словарю с макросами
dataFile = "C:\p.yu\Monitoring\Zabbix.Operations\zbx.create.macros\macrosData.txt"
a = read_file_to_dict(dataFile)


group = zapi.host.get( hostids = 13604 , output=['itemid', 'name'])
for host in group:
    items = zapi.item.get(hostids=host['hostid'])
    for item in items:
        itemid = item['itemid']
        print(item['key_'])
        item = (item['key_'].replace('[', ',').replace(']', '')).split(',')
        try:
            param1 = get_key(a, item[1])
            param2 = get_key(a, item[2])
            param3 = get_key(a, item[3])
            if param1 and param2 and param3:
                newKey = 'balance.py[' + param1 + ',' + param2 + ',' + param3 + ']'
                print(newKey)
                zapi.item.update(itemid=itemid, key_=newKey)
            else:
                print('Макросы для замены отсутсвуют')
        except Exception:
            print('')
            print(item)
