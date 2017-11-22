#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
# Zabbix connect
from pyzabbix import ZabbixAPI
zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'
zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)

# hostid = argv[1]
# hostid = '14595'
hostname = argv[1]
# hostname = 'www.eurodate.com test'



def zabbix_service_add(hostname):
    try:
        group = zapi.host.get(output=['itemid', 'name'],\
                              filter={'host': hostname})
        # print(group)
        for host in group:
            a = zapi.hostgroup.massadd(groups={"groupid": "216"},\
                                     hosts={'hostid': host['hostid']})
            print('Хост переведен в режим "Обслуживание"')
            print(a)
    except Exception:
        print("Переключение завершилось неудачно.\
              Обратитесь к администратору мониторинга!")

if hostname == 'www.eurodate.com test':
    zabbix_service_add(hostname)
else:
    print('Данный скрипт запрещено использовать на хостах кроме\
          "www.eurodate.com test"')
