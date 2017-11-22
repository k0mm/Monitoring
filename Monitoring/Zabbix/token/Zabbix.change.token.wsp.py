from pyzabbix import ZabbixAPI


def zabbix_token_change_balance (hostid,zbxmacroname,token):
    try:
        oldMacro = zapi.usermacro.get(hostids=hostid, search={'macro': zbxmacroname})
        if ((oldMacro[0])['value']) == token:
            print('Замена не удалась! Макрос',zbxmacroname,'уже имеет значение',token)
        else:
            print(zapi.usermacro.update(hostmacroid=(oldMacro[0])['hostmacroid'], hostid=(oldMacro[0])['hostid'], macro=zbxmacroname, value=token))
    except Exception:
        print ('Для макроса', zbxmacroname, 'не удалось поменять значение')

#Zabbix connect
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'
zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)

hostid = '13604'

AMO_Girl_Token = '6509126a-4034-4dcf-bd6f-7c810026e69a'
AMO_Man_Token = 'ccbe3c3b-fc47-4e42-8440-24b289e6cc7d'
DC_Man_Token = '2b15e29f-4376-40b4-bc84-1ed7ef763898'

# AMO
zabbix_token_change_balance(hostid, '{$CP.CR.AMO.WSP.GIRL.TOKEN}', AMO_Girl_Token)
zabbix_token_change_balance(hostid, '{$CP.CR.AMO.WSP.MAN.TOKEN}', AMO_Man_Token)
# DC
zabbix_token_change_balance(hostid, '{$CP.CR.DC.WSP.MAN.TOKEN}', DC_Man_Token)
