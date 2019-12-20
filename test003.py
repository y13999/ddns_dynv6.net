import requests
head = {
        'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
    }
url='http://dynv6.com/api/update?hostname=x13999.dynv6.net&ipv6=2409:875c:5c30:10:d516:84e2:52da:394e&token=XHs1GqoHZF8XQxy1VPMiYxy1sYe3ex'
respone = requests.get(url,headers=head)
print(respone)