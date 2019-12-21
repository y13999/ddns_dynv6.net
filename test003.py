#open(file, mode='r+', buffering=-1, encodingutf8, errors=None, newline=None, closefd=True, opener=None)
import os
import re
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


try:
    if os.path.exists(file_name_ini):
        file_001=open(file_name_ini, mode='r+', encoding='utf-8')
        ff1=file_001.read()
        Domain_name =get_pat(dn,ff1)
        Benutzer_name = get_pat(bn,ff1)
        print('当前记录的域名是:',Domain_name)
        print('当前记录的密钥是:',Benutzer_name)
        print('如果要修改域名或者密钥，请输入y，如果不需要修改，请输入n(15秒后默认输入n）：')
        t=threading.Thread(target=input_fution,args=(context,))
        t.start()
        t.join(5)
        print(context)
        print(t)


    else:
        file_001=open(file_name_ini, mode='a+', encoding='utf-8')
        Domain_name = input('请输入域名：')
        Benutzer_name = input('请输入密钥：')
        file_001.write('Domainname ='+Domain_name+'\n')
        file_001.write('Benutzername ='+Benutzer_name+'\n')
        file_001.flush()

finally:
    if file_001:
        file_001.close()




###get keyboard input and timeout =5
import sys, time, msvcrt
def readInput(default='n', timeout=5):
    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche()
            if ord(chr) == 13:  # enter_key
                break
            elif ord(chr) >= 32:  # space_char
                input += chr

        if len(input) == 0 and (time.time() - start_time) > timeout:
            break
        print(input)
    ''  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default


print(readInput())