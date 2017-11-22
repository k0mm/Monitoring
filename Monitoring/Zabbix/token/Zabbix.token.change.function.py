from pyzabbix import ZabbixAPI


# Function
def zabbix_token_change(hostname, macroname, token):
    zbxmacroname = gender + ".TOKEN"
    group = zapi.host.get( output=['itemid', 'name'], search={'name': hostname})
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro': zbxmacroname})
        for macro in macros:
            print(
                zapi.usermacro.update(
                    hostmacroid=macro['hostmacroid'], hostid=macro['hostid'], macro=macroname,
                                        value=token))


#Zabbix connect
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '------------'

zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)


zabbix_token_change(value1,value2,value3)