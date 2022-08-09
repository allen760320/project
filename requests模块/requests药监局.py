#codeing:utf-8
import requests
import json
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
id_list = []
all_data_list = []
for page in range(1,6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_ids = requests.post('http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList',headers=head,data=data).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
for id in id_list:
    data= {
        'id':id
    }
    detail_json = requests.post('http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById',headers=head,data=data).json()
    #print(detail_json)
    all_data_list.append(detail_json)
fp = open('alldata.json', 'w', encoding='utf-8')
json.dump(all_data_list,fp=fp,ensure_ascii=False)
print('over!')