from pyzabbix import ZabbixAPI

# Zabbix connect
zbxurl = 'http://monitoring'
zbxname = '*********'
zbxpass = '*********'

try:
    zapi = ZabbixAPI(zbxurl)
    zapi.login(zbxname, zbxpass)
    print('Удалось подключиться к серверу Zabbix')
except Exception:
    print('Не удалось подключиться к серверу Zabbix')

def get_key(dict , value):
    for k, v in dict.items():
        if v in value:
            return k

def read_file_to_dict(dataFile):
    valuesDict = {}
    for line in open(dataFile):
        key, value = line.split('\t')
        # value = value.rstrip
        valuesDict[key] = value.rstrip()
    return valuesDict


dataFile = "C:\p.yu\Monitoring\Zabbix.Operations\zbx.create.macros\\trigger.update\\triggerData.txt"
hostid = 13604

a = read_file_to_dict(dataFile)
print(a)
i = 0
group = zapi.host.get( hostids = hostid , output=['itemid', 'name'])
for host in group:
    items = zapi.item.get(hostids=host['hostid'])
    for item in items:
        itemid = item['itemid']
        triggers = zapi.trigger.get(itemids=itemid)
        for trigger in triggers:
            print(trigger)
            macroKey = get_key(a, trigger['description'])
            if macroKey:
                macroValue = a[macroKey]
                i = i + 1
                newDecription = trigger['description'].replace(macroValue,macroKey)
                newComment = trigger['comments'].replace(macroValue,macroKey)
                zapi.trigger.update( triggerid=trigger['triggerid'], comments=newComment, description=newDecription)
                print('=========================================================')
print(i)
