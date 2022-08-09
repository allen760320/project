#-*- coding = utf-8 -*-

from bs4 import BeautifulSoup
import re
import sqlite3
import xlwt
import urllib.request,urllib.error

savepath = "./"
def main():
    baseurl = "https://movie.douban.com/top250?start="


def getData(baseurl):
    datalist = []
    return datalist

def askURL(url):
    head = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80 Safari / 537.36 Edg / 98.0.1108.50"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""






def saveData(savepath):
    print("save")