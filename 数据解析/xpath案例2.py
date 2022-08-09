#codeing:utf-8
import requests
from lxml import etree
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
url = "http://www.aqistudy.cn/historydata/"
page_text = requests.get(url=url,headers=head).text
tree = etree.HTML(page_text)
# host_li_list = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
# all_city_names = []
# for li in host_li_list:
#     host_city_names = li.xpath('./a/text()')[0]
#     all_city_names.append(host_city_names)
# city_names_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li')
# for li in city_names_list:
#     city_names = li.xpath('./a/text()')[0]
#     all_city_names.append(city_names)
#
# print(all_city_names,len(all_city_names))
all_city_names = []
a_list = tree.xpath('/html/body/div[3]/div/div[1]//div[2]/ul//li')
for a in a_list:
    city_names = a.xpath('./a/text()')[0]
    all_city_names.append(city_names)
print(all_city_names,len(all_city_names))
