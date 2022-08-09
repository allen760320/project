#codeing:utf-8
import requests
from bs4 import BeautifulSoup
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
url = "https://www.shicimingju.com/book/sanguoyanyi.html"
page_text = requests.get(url=url,headers=head).content.decode("utf-8")
#print(page_text.content.decode("utf-8"))
soup = BeautifulSoup(page_text,'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open('./sanguo.txt','w',encoding='utf-8')
for li in li_list:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com'+li.a['href']
    detail_page_text = requests.get(url=detail_url,headers=head).content.decode("utf-8")
    detail_soup = BeautifulSoup(detail_page_text,'lxml')
    div_tag = detail_soup.find('div',class_='chapter_content')
    content = div_tag.text
    fp.write(title+':'+content+'\n')
    print(title,'爬取成功')
