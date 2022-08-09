#codeing:utf-8
import requests
from lxml import etree
import csv
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
url = "https://dt.8684.cn/xz"
page_text = requests.get(url=url,headers=head).content.decode('utf-8')
#print(page_text)

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="ib-box"]/ul[@class="ib-mn cm-mn"]/li')

for li in li_list:
    detail_url = 'https://dt.8684.cn' + li.xpath('./a[1]/@href')[0]
    print(detail_url)
