import os
net_dict={}
data=os.popen('ipconfig /all').readlines()
for line in data:
    if "网适配器" in line:
        #print line[line.index('器')+3:].split(':')[0],
        interface=line[line.index('器')+3:].split(':')[0]
        net_dict[interface]=''
    if 'IPv4' in line:
        #print line.split(":")[1]
        ip=line.split(":")[1].strip().split('(')[0]
        net_dict[interface]=ip
for net in net_dict.keys():
    print(net+":"+net_dict[net])
##############################################################################
import socket
def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    print(get_host_ip())
    # 获取计算机名称
    hostname = socket.gethostname()
    print(hostname)
    # 获取本机IP
    ip = socket.gethostbyname(hostname)
    print(ip)
    addrs = socket.getaddrinfo(hostname, None)
    print(addrs)
    for item in addrs:
        print(item)

    addrs = socket.getaddrinfo(socket.gethostname(), None)
    for item in addrs:
        print(item)
    # 仅获取当前IPV4地址
    print('当前主机IPV4地址为:' + [item[4][0] for item in addrs if ':' not in item[4][0]][0])
    # 同上仅获取当前IPV4地址
    for item in addrs:
        if ':' not in item[4][0]:
            print('当前主机IPV4地址为:' + item[4][0])
            break