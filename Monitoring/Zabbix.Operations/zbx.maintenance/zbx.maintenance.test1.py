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

hostname = argv[1]
# hostid = '14595'
# hostname = 'www.eurodate.com test'


def zabbix_token_print(hostname):
    group = zapi.host.get(output=['itemid', 'name'], filter={'host': hostname})
    print(group)
    for host in group:
        macros = zapi.usermacro.get(hostids=host['hostid'])
        for macro in macros:
            print(macro)

zabbix_token_print(hostname)
