#codeing:utf-8
import requests
import re
import csv
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
response = requests.get("https://movie.douban.com/top250",headers=head)
page_content = response.text
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)</span>',re.S)

result = obj.finditer(page_content)
f = open("data.csv",mode="w",encoding="utf-8")
csvwrite = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("year").strip())
    # print(it.group("score"))
    # print(it.group("num"))
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwrite.writerow(dic.values())
f.close()
print("over")
