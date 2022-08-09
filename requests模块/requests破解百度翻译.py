#codeing:utf-8
import requests
import json
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
word = input('enter a word:')
data = {'kw':word}
response = requests.post('https://fanyi.baidu.com/sug',data=data,headers=head)
dic_obj = response.json()
print(dic_obj)
fp = open(f'./{word}.json','w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
print('over!')