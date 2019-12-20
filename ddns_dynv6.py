import socket
import re
#import requests
def get_IPv4():
    # 获取计算机名称
    hostname = socket.gethostname()
    # 获取本机IP
    ipv4_addr = socket.gethostbyname(hostname)
    try:
        return ipv4_addr
    except:
        return ''
def get_IPv6():
    # 获取计算机名称
    hostname = socket.gethostname()
    addrs = socket.getaddrinfo(hostname, None)
    # 仅获取当前IPV6地址
    for item in addrs:
        if ':' in item[4][0]:
            if item[4][3] > 0:
                ipv6_addr=item[4][0]
                break
    try:
        return ipv6_addr
    except:
        return ''

if __name__ == '__main__':
    host_name=socket.gethostname()
    ipv4_addr=get_IPv4()
    ipv6_addr=get_IPv6()
    print(ipv4_addr)
    print(ipv6_addr)
    url_ip='http://dynv6.com/api/update?hostname='
    Domainname='y13999.dynv6.net'
    Benutzername='XHs1GqoHZF8XQxy1VPMiYxy1sYe3ex'
    token_mark='token='
    ip_type='ipv6='
    and_mark='&'
    url_all=url_ip+Domainname+and_mark+ip_type+ipv6_addr+and_mark+token_mark+Benutzername
    print(url_all)


