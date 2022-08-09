#codeing:utf-8
import requests
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
kw = input('enter a word:')
response = requests.get(f'https://www.baidu.com/s?word={kw}&tn=92363592_hao_pg',headers=head)
page_text = response.text
filename = kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print('保存成功')
