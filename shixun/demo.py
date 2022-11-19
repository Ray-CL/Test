# -*- coding=utf-8 -*-
# Time:2022/7/12 14:12
# Author:Ray
# File:demo.py
# Software:PyCharm
from bs4 import BeautifulSoup
import re
import urllib.request
import random


class Douban:

    def __init__(self, path, url, head):
        self.url = url
        self.path = path
        self.head = head

    def getData(self):
        req = urllib.request.Request(url=self.url, headers=self.head, method="POST")
        data = urllib.request.urlopen(req)
        return data


def getAgent():
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
                  "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"]
    headers = {"User-Agent": random.choice(user_agent)}
    return headers


if __name__ == "__main__":
    path = "./豆瓣电影Top250.html"
    Url = "http://movie.douban.com/top250?start="
    for i in range(0, 10):
        url = Url + str(i * 25)
        temp = Douban(path, url, getAgent())
        data = temp.getData()
        data_cont = data.read().decode("UTF-8")
        file = open(temp.path, "a", encoding="UTF-8")
        file.write(data_cont)
        file.close()
