#!/usr/bin/env python
#
import datetime
import pythonwhois  # i'm using this http://cryto.net/pythonwhois
domains = ['anastasiadate.com']
for dom in domains:
    details = pythonwhois.get_whois(dom)
    print(int(((details['expiration_date'])[0] - datetime.datetime.today()).total_seconds()))
