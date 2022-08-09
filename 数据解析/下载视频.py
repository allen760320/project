#codeing:utf-8
import requests
from lxml import etree
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Referer': 'https://pearvideo.com/video_1750705'
}
url = "https://pearvideo.com/video_1750705"
contID = url.split("_")[1]
videourl = f"https://pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.16467031468916504"
dic = requests.get(url=videourl,headers=head).json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime,f"cont-{contID}")
print(srcUrl)
