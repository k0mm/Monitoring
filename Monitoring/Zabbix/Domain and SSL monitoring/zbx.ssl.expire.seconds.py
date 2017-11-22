import OpenSSL
import ssl
from datetime import datetime
domain = 'www.anastasiadate.com'
port = 443
timenow = (datetime.today())


def check_ssl_expdate(domain, port):
    try:
        cert = ssl.get_server_certificate((domain, port))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,
                                               cert)
        return(datetime.strptime(x509.get_notAfter().decode('ascii'),
                                 '%Y%m%d%H%M%SZ'))
    except Exception:
        return('0')


exptime = (check_ssl_expdate(domain, port) - timenow).total_seconds()
print(int(exptime))
