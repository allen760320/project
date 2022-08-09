#codeing:utf-8
import requests
response = requests.get('https://www.baidu.com/?tn=92363592_hao_pg')
page_text = response.content.decode('utf-8')
print(page_text)
with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('爬取数据结束！')
