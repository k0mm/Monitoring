#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from pyzabbix import ZabbixAPI, ZabbixAPIException


zbxurl = 'http://monitoring'
zbxname = 'api-scripts'
zbxpass = '99iFdurfck2323'
logfile = '/var/log/zabbix/get.count.item.like.item_key.host.log'

host_host = sys.argv[1]
key_like = sys.argv[2]
value_eq = sys.argv[3]
my_item_key = 'get.count.item.like.item_key.host.py[' + host_host + ',' + key_like + ',' + value_eq + ']'

zapi = ZabbixAPI(zbxurl)
zapi.login(zbxname, zbxpass)

items = zapi.item.get(output=['itemid', 'name', 'lastvalue', 'key_', 'lastclock'], host=host_host, monitored='true', search={'key_': key_like})

i=0
for item in items:
    if item['lastvalue'] != value_eq and item['lastclock'] != '0' and item['key_'] !=  my_item_key:
        i += 1
 print (i)

