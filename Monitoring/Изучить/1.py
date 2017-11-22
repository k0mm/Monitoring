#!/usr/bin/env python
#
# Usage:
# python check_domain.py -d DOMAIN
import whois
from datetime import datetime

from sys import exit
from optparse import OptionParser


def check_domain(domain):
    q = whois.query(domain)
    if (q.expiration_date - datetime.now()).days <= 30:
        print "CRITICAL: Domain: {0} expires on {1}".format(domain, q.expiration_date)
        exit(2)
    print "OK: Domain: {0} expires on {1}".format(domain, q.expiration_date)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--domain",
                      dest="domain", help="Domain to monitor expiry date")
    (options, args) = parser.parse_args()
    if not options.domain:
        print parser.print_help()
        exit(0)

    check_domain(options.domain)
