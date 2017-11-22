from pyzabbix import ZabbixAPI
#import re
import sys
#Simple log
#LogPath = 'C:\\temp\\log.txt'
#sys.stdout = open(LogPath,'w')

#Zabbix connect
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'

zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)

#Token mask
#tokenredexp = re.compile('[\d\w]+-[\d\w]+-[\d\w]+-[\d\w]+-[\d\w]+')

#Static variables
zbxgroupid=224 #  Критерий поиска только по группе ИС - WSP
zbxmacroname = 'token'
zbxhostname = "test"
zbxnewtoken = 'new_token_11111111'

#input args
#try:
#    zbxhostname = sys.argv[1]
#    zbxmacroname = sys.argv[2]
#    zbxnewtoken = sys.argv[3]

#Function
group = zapi.host.get(groupids=224, output=['itemid','name'],search={'name': zbxhostname})
for host in group:
    macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro':zbxmacroname})
    print (macros)
    #for macro in macros:
    #    print(zapi.usermacro.update(hostmacroid=macro['hostmacroid'],hostid=macro['hostid'],macro=macro['macro'],value=zbxnewtoken))
