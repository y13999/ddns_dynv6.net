import socket
import re
import os
import requests
import _thread
import threading
import time

def input_fution(context):
    context['data']=input('')

def get_pat(pat, doc):
    res_list = re.findall(pat, doc)
    try:
        return res_list[0]
    except:
        return ''
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
        print('找不到本机IPv6.')
        rr=input('请手动输入IPv6地址：')
        return rr

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
        return print('更新ddns出错，请检查')

def url_toget(Domain_name,Benutzer_name,ipv6_addr):
    token_mark='token='
    ip_type='ipv6='
    and_mark = '&'
    url_ip='http://dynv6.com/api/update?hostname='
    url_all = url_ip + Domain_name + and_mark + ip_type + ipv6_addr + and_mark + token_mark + Benutzer_name
    #print('要提交的ddsn的url为：',url_all)
    return url_all

if __name__ == '__main__':
    #定义各种参数
    file_name_ini = 'ddns_dynv6.ini'
    Domain_name = ''
    Benutzer_name = ''
    file_001 = ''
    dn = r'Domainname.*\s*=(.*?)\n'
    bn = r'Benutzername.*\s*=(.*?)\n'
    context = {'data': 'n'}
    #开始
    ipv6_addr=get_ipv6_addr()
    print('本机首选IPv6地址是：',ipv6_addr)
    if ipv6_addr[0:4]=='fe80':
        print('本机IPv6地址是私网地址，请检查IPv6地址情况：')
        ipv6_addr = input('请手动输入IPv6地址：')
    #配置文件读取
    try:
        if os.path.exists(file_name_ini):
            file_001 = open(file_name_ini, mode='r+', encoding='utf-8')
            ff1 = file_001.read()
            Domain_name = get_pat(dn, ff1)
            Benutzer_name = get_pat(bn, ff1)
            print('当前记录的域名是:', Domain_name)
            print('当前记录的密钥是:', Benutzer_name)
            print('如果要修改域名或者密钥，请输入y，如果不需要修改，请输入n(10秒后默认输入n）：')
            t = threading.Thread(target=input_fution, args=(context,))
            t.start()
            t.join(10)
            #print(context['data'])
            if context['data']=='y':
                Domain_name = input('请输入域名：')
                Benutzer_name = input('请输入密钥：')
                ipv6_addr001=input('请输入新IPv6，如果不修改请回车')
                if ipv6_addr001!='':
                    ipv6_addr=ipv6_addr001
                file_001.close()
                file_001 = open(file_name_ini, mode='w+', encoding='utf-8')
                file_001.write('Domainname=' + Domain_name + '\n')
                file_001.write('Benutzername=' + Benutzer_name + '\n')
                file_001.write('IPv6=' + ipv6_addr + '\n')
                file_001.flush()
                os.system('cls')
                print('新域名是:', Domain_name)
                print('新密钥是:', Benutzer_name)
                print('新IPv6是:', ipv6_addr)

        else:
            file_001 = open(file_name_ini, mode='a+', encoding='utf-8')
            Domain_name = input('请输入域名：')
            Benutzer_name = input('请输入密钥：')
            file_001.write('Domainname=' + Domain_name + '\n')
            file_001.write('Benutzername=' + Benutzer_name + '\n')
            file_001.write('IPv6=' + ipv6_addr + '\n')
            file_001.flush()
    finally:
        if file_001:
            file_001.close()

    url_all=url_toget(Domain_name,Benutzer_name,ipv6_addr)
    for i in range(525600):#1年的分钟数
        #print('round:',i)
        new_ipv6_addr=get_ipv6_addr()
        if i==0:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),end='')
            print('正在提交ddns和对应的IPv6的更新，请等待：')
            url_all = url_toget(Domain_name, Benutzer_name, ipv6_addr)
            print('要提交的ddsn的url为：', url_all)
            respone = get_dynv6_html_doc(url_all)
            print('结果是：',end='\t')
            print(respone)
            if 'unchange' in respone:
                print('当前IPv6和原来的ddns一致，没有更改')
            elif 'addresses updated'in respone:
                print('修改ddns成功')
            elif 'invalid authentication token' in respone:
                print('密钥出错，请检查密钥')
                os.system("pause")
                sys.exit()
            elif 'zone not found' in respone:
                print('域名出错，请检查域名')
                os.system("pause")
                sys.exit()
            else:
                print('未知问题，请关闭程序检查各项参数')
        elif new_ipv6_addr != ipv6_addr:
            os.system('cls')
            print('发现新IPv6和记录的IPv6不一致，重新提交ddns:')
            print('当前域名是:', Domain_name)
            print('当前密钥是:', Benutzer_name)
            print('新IPv6是:', new_ipv6_addr)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), end='')
            print('正在提交ddns和对应的IPv6的更新，请等待：')
            url_all = url_toget(Domain_name, Benutzer_name, new_ipv6_addr)
            print('要提交的ddsn的url为：', url_all)
            respone = get_dynv6_html_doc(url_all)
            print('结果是：',end='\t')
            print(respone)
            if 'unchange' in respone:
                print('当前IPv6和原来的ddns一致，没有更改')
            elif 'addresses updated'in respone:
                print('修改ddns成功')
            elif 'invalid authentication token' in respone:
                print('密钥出错，请检查密钥')
                os.system("pause")
                sys.exit()
            elif 'zone not found' in respone:
                print('域名出错，请检查域名')
                os.system("pause")
                sys.exit()
            else:
                print('未知问题，请关闭程序检查各项参数')
        for i01 in range(60):
             if i01%2==0:
                 print('\r程序还在运行中，自动检测本机IPv6变化，已运行',i,'分钟，继续运行计时：',i01,end='')
                 time.sleep(2)




