import requests
import json

def QueryId(idnum,name):
    url = 'http://emsc.cx580.com:8092/emsc-pub-api/q/queryIdCard.ajax'
    v = {'inputValue':'','acceptNbr':idnum,'idCardName':name}
    res = requests.post(url=url,data=v)
    json_str = res.content.decode('utf-8')
    s = json.loads(json_str)
    info_list = s['body']['infoList']
    for i in info_list:
        print(i['title'])

QueryId('身份证号','姓名')