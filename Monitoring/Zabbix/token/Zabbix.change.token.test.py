from pyzabbix import ZabbixAPI


# {'hostmacroid': '5388', 'hostid': '14168', 'macro': '{$PT.CP.CHAT.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5400', 'hostid': '14168', 'macro': '{$PT.CP.MAIL.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5409', 'hostid': '14168', 'macro': '{$PT.CP.PROFILE.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5645', 'hostid': '14176', 'macro': '{$PT.CP.CHAT.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5657', 'hostid': '14176', 'macro': '{$PT.CP.MAIL.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5666', 'hostid': '14176', 'macro': '{$PT.CP.PROFILE.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5681', 'hostid': '14177', 'macro': '{$PT.CP.CHAT.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5693', 'hostid': '14177', 'macro': '{$PT.CP.MAIL.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '5702', 'hostid': '14177', 'macro': '{$PT.CP.PROFILE.GIRL.TOKEN}', 'value': 'deae3e63-d77e-4a97-9fd9-f76a4753f3f6'}
# {'hostmacroid': '6967', 'hostid': '14518', 'macro': '{$PT.CP.CHAT.GIRL.TOKEN}', 'value': '910802ec-0c41-414d-b6b1-122cfd65ca9a'}
# {'hostmacroid': '6979', 'hostid': '14518', 'macro': '{$PT.CP.MAIL.GIRL.TOKEN}', 'value': '910802ec-0c41-414d-b6b1-122cfd65ca9a'}
# {'hostmacroid': '6988', 'hostid': '14518', 'macro': '{$PT.CP.PROFILE.GIRL.TOKEN}', 'value': '910802ec-0c41-414d-b6b1-122cfd65ca9a'}

# Function
def zabbix_token_change(hostname, gender, token):
    zbxmacroname = gender + ".TOKEN"
    group = zapi.host.get(groupids=224, output=['itemid', 'name'], search={'name': hostname})
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro': zbxmacroname})
        for macro in macros:
            print(
                zapi.usermacro.update(
                    hostmacroid=macro['hostmacroid'], hostid=macro['hostid'], macro=macro['macro'],
                                        value=token))


# Function
def zabbix_token_print(hostname, gender,token):
    print (token)
    zbxmacroname = gender + ".TOKEN"
    group = zapi.host.get(groupids=224, output=['itemid', 'name'], search={'name': hostname})
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro': zbxmacroname})
        for macro in macros:
            print(macro)


# Zabbix connect
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'
zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)

DC_Man_Token = 1
DC_Girl_Token = 1
RB_Man_Token =1
RB_Girl_Token =1
AF_Man_Token =1
AF_Girl_Token =1
AMO_Man_Token =1
AMO_Girl_Token =1
AR_Man_Token =1
AR_Girl_Token =1
DMA_Man_Token =1
DMA_Girl_Token =1
EU_Man_Token =1
EU_Girl_Token =1
FW_Man_Token =1
FW_Girl_Token =1
SHA_Man_Token =1
SHA_Girl_Token =1
YCD_Man_Token =1
YCD_Girl_Token =1
YTM_Man_Token =1
YTM_Girl_Token =1

zabbix_token_print ('dating','man',DC_Man_Token)
zabbix_token_print ('dating','girl',DC_Girl_Token)
zabbix_token_print ('russian','man',RB_Man_Token)
zabbix_token_print ('russian','girl',RB_Girl_Token)
zabbix_token_print ('african','man',AF_Man_Token)
zabbix_token_print ('african','girl',AF_Girl_Token)
zabbix_token_print ('amolatina','man',AMO_Man_Token)
zabbix_token_print ('amolatina','girl',AMO_Girl_Token)
zabbix_token_print ('arabian','man',AR_Man_Token)
zabbix_token_print ('arabian','girl',AR_Girl_Token)
zabbix_token_print ('datemyage','man',DMA_Man_Token)
zabbix_token_print ('datemyage','girl',DMA_Girl_Token)
zabbix_token_print ('eurodate','man',EU_Man_Token)
zabbix_token_print ('eurodate','girl',EU_Girl_Token)
zabbix_token_print ('flirtwith','man',FW_Man_Token)
zabbix_token_print ('flirtwith','girl',FW_Girl_Token)
zabbix_token_print ('sharekalomre','man',SHA_Man_Token)
zabbix_token_print ('sharekalomre','girl',SHA_Girl_Token)
zabbix_token_print ('yourchristiandate','man',YCD_Man_Token)
zabbix_token_print ('yourchristiandate','girl',YCD_Girl_Token)
zabbix_token_print ('yourtravelmates','man',YTM_Man_Token)
zabbix_token_print ('yourtravelmates','girl',YTM_Girl_Token)