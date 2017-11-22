from pyzabbix import ZabbixAPI

#Function
def zabbix_token_change (hostname,gender,token):
    zbxmacroname = gender + ".TOKEN"
    group = zapi.host.get(groupids=224, output=['itemid','name'],search={'name': hostname})
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro':zbxmacroname})
        for macro in macros:
            print(zapi.usermacro.update(hostmacroid=macro['hostmacroid'], hostid=macro['hostid'], macro=macro['macro'],value=token))

# Function
def zabbix_token_print(hostname, gender):
    zbxmacroname = gender + ".TOKEN"
    group = zapi.host.get(groupids=224, output=['itemid', 'name'], search={'name': hostname})
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'], search={'macro': zbxmacroname})
        for macro in macros:
            print(macro)

def zabbix_token_change_balance (hostid,zbxmacroname,token):
    try:
        oldMacro = zapi.usermacro.get(hostids=hostid, search={'macro': zbxmacroname})
        test=(oldMacro[0])['hostmacroid']
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



#Tokens
DC_Man_Token ='8a580b4b-6c48-4a57-90c1-1b72c30a9166'
DC_Girl_Token ='a25789f1-938e-42db-a4bd-5eb116328d44'
RB_Man_Token ='693c6d1b-2ea3-4e30-937b-f97a094a57d0'
RB_Girl_Token ='95bd1714-5fd8-45a1-9ad9-ddcb58f4b6f9'
AF_Man_Token ='163329e5-2565-4b31-9492-d28ad553e01c'
AF_Girl_Token ='970f1d6e-0351-460b-94cd-41813674a3a6'
AMO_Man_Token ='d0a29c48-d1a1-4ce1-ba44-255c01ea7359'
AMO_Girl_Token ='7040428e-17cc-4129-826b-2852b03b76dd'
AR_Man_Token ='65874ca4-0118-4b27-9d56-cd94347144b3'
AR_Girl_Token ='910802ec-0c41-414d-b6b1-122cfd65ca9a'
DMA_Man_Token ='d2f27931-87d2-427c-bcbf-65ebbeb408aa'
DMA_Girl_Token ='84415890-54e5-41f4-9e8f-bdd61b99f4da'
EU_Man_Token ='35307f2c-be93-43c8-8909-deda98780744'
EU_Girl_Token ='9399746b-3891-44b3-b663-e8b949849781'
FW_Man_Token ='525a6a96-c099-4b72-9677-a66d4dba245e'
FW_Girl_Token ='e47f72e8-d3f8-4741-9872-10afef04dda9'
SHA_Man_Token ='6c0100a0-a5d7-4941-83e7-ddf0076b197c'
SHA_Girl_Token ='3ce674ab-1410-4e3c-990e-2b1bf8113571'
YCD_Man_Token ='2d6aaab2-3ef3-46f9-a644-d196459e629f'
YCD_Girl_Token ='95da8bcb-b676-4b3a-84c0-a7809f8d79eb'
YTM_Man_Token ='f4b53d09-36c1-4900-84e1-ef8478a84523'
YTM_Girl_Token ='b51630d5-1336-421c-a225-10c6e23c5cd2'

# # #DC
# zabbix_token_change ('dating','man',DC_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.DC.ZBX.MAN.TOKEN}', DC_Man_Token)
# zabbix_token_change ('dating','girl',DC_Girl_Token)
# # #RB
# zabbix_token_change ('russian','man',RB_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.RB.WSP.MAN.TOKEN}', RB_Man_Token)
# zabbix_token_change ('russian','girl',RB_Girl_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.NRB.WSP.GIRL.TOKEN}', RB_Girl_Token)
# # #AF
# zabbix_token_change ('african','man',AF_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.AFR.WSP.MAN.TOKEN}', AF_Man_Token)
# zabbix_token_change ('african','girl',AF_Girl_Token)
# # #AMO
# zabbix_token_change ('amolatina','man',AMO_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.AMO.ZBX.MAN.TOKEN}', AMO_Man_Token)
# zabbix_token_change ('amolatina','girl',AMO_Girl_Token)
# #AR
# zabbix_token_change ('arabian','man',AR_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.ARB.WSP.MAN.TOKEN}', AR_Man_Token)
# zabbix_token_change ('arabian','girl',AR_Girl_Token)
# #DMA
# zabbix_token_change ('datemyage','man',DMA_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.DMA.WSP.MAN.TOKEN}', DMA_Man_Token)
# zabbix_token_change ('datemyage','girl',DMA_Girl_Token)
# #EU
# zabbix_token_change ('eurodate','man',EU_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.ED.WSP.MAN.TOKEN}', EU_Man_Token)
# zabbix_token_change ('eurodate','girl',EU_Girl_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.ED.WSP.GIRL.TOKEN}', EU_Girl_Token)
# #FW
# zabbix_token_change ('flirtwith','man',FW_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.FW.WSP.MAN.TOKEN}', FW_Man_Token)
# zabbix_token_change ('flirtwith','girl',FW_Girl_Token)
# # SHA
# zabbix_token_change ('sharekalomre','man',SHA_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.SHA.WSP.MAN.TOKEN}', SHA_Man_Token)
# zabbix_token_change ('sharekalomre','girl',SHA_Girl_Token)
# #YCD
# zabbix_token_change ('yourchristiandate','man',YCD_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.YCD.WSP.MAN.TOKEN}', YCD_Man_Token)
# zabbix_token_change ('yourchristiandate','girl',YCD_Girl_Token)
# #YTM
# zabbix_token_change ('yourtravelmates','man',YTM_Man_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.YTM.WSP.MAN.TOKEN}', YTM_Man_Token)
# zabbix_token_change ('yourtravelmates','girl',YTM_Girl_Token)
# zabbix_token_change_balance('13604', '{$CP.CR.YTM.WSP.GIRL.TOKEN}', YTM_Girl_Token)
