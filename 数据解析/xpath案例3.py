#codeing:utf-8
import requests
from lxml import etree
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
page_text = requests.get(url=url,headers=head).text
#print(page_text)
tree = etree.HTML(page_text)
li_list = tree.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for li in li_list:
    title = "saas".join(li.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
    print(title)

