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