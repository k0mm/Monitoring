#!/usr/bin/env python
#
# Usage:
# python check_domain.py -d DOMAIN
import whois
from datetime import datetime

domain = 'google.com'
q = whois.query(domain)

print(q)
