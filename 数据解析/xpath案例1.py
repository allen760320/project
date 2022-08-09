#codeing:utf-8
import requests
from lxml import etree
import os
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
url = "https://pic.netbian.com/4kmeinv/"
page_text = requests.get(url=url,headers=head).text
#print(page_text)
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
if not os .path.exists('./piclibs'):
    os.mkdir('./piclibs')
for li in li_list:
    img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    #通用处理中文乱码的解决方案
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(url=img_src,headers=head).content
    img_path = 'piclibs/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功')
