import socket
import re
import os
import requests
def find_all_by_pat(pat, string):
    res = re.findall(pat, string)
    return res

def get_addr(pat, doc):
    res_list = find_all_by_pat(pat, doc)
    try:
        return res_list[0]
    except:
        return ''
def get_ipv6_addr():
    data=os.popen('ipconfig /all').readlines()
    i=[]
    j=[]
    k=''
    for d in data:
        if 'IPv6' in d:
            i.append(d)
            #print(i)
            for n in range(len(d)):
                if d[n]!=' ':
                    k=k+d[n]
                j.append(k)
    key_key = r'...:(.*)\('
    rr=''
    for i in range(len(j)):
        if j[i][0:4]=='IPv6':
            rr=get_addr(key_key,k)
    try:
        return rr
    except:
        return print('找不到IPv6')

def get_dynv6_html_doc(url):
    #pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
    head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
    #resopnse = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
    resopnse = requests.get(url, headers=head)
    resopnse.encoding = 'utf-8'
    html_doc = resopnse.text
    try:
        return html_doc
    except:
        return print('提交IPv6出错，请检查')

if __name__ == '__main__':
    #host_name=socket.gethostname()
    #ipv4_addr=get_IPv4()
    ipv6_addr=get_ipv6_addr()
    print('本机首选IPv6地址是：',ipv6_addr)
    if ipv6_addr[0:4]=='fe80':
        print('本机IPv6地址是私网地址，请检查IPv6地址情况：')
    url_ip='http://dynv6.com/api/update?hostname='
    Domainname='x13999.dynv6.net'
    Benutzername='XHs1GqoHZF8XQxy1VPMiYxy1sYe3ex'
    token_mark='token='
    ip_type='ipv6='
    and_mark='&'
    url_all=url_ip+Domainname+and_mark+ip_type+ipv6_addr+and_mark+token_mark+Benutzername
    print(url_all)
    #url = 'http://dynv6.com/api/update?hostname=x13999.dynv6.net&ipv6=2409:875c:5c30:10:d516:84e2:52da:394e&token=XHs1GqoHZF8XQxy1VPMiYxy1sYe3ex'
    respone = get_dynv6_html_doc(url_all)
    print(respone)


