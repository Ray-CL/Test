# -*- coding=utf-8 -*-
# Time:2022/10/1 12:05
# Author:Ray
# File:豆瓣Top250.py
# Software:PyCharm
import urllib.request
import random
import re
from bs4 import BeautifulSoup
import xlwt


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
    """
    正则表达
    """
    num = 1
    path = "./豆瓣电影Top250.html"
    Url = "http://movie.douban.com/top250?start="
    find_link = re.compile('<a href="(.*?)">')
    find_img = re.compile('<img.*src="(.*?)"')
    find_title = re.compile('<span class="title">(.*?)</span>')
    find_rate = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
    find_people = re.compile('<span>(.*?)评价</span>')
    find_Con = re.compile('<span class="inq">(.*?)</span>')
    find_Bd = re.compile('<p class="">(.*?)主.*</p>', re.S)
    file = open("./豆瓣Top250电影详情.txt", "a", encoding="UTF-8")
    """excel初始化"""
    workbook = xlwt.Workbook(encoding="UTF-8")
    worksheet = workbook.add_sheet("sheet", cell_overwrite_ok=True)
    col = ["电影名字", "电影链接", "电影图片链接", "电影评分", "电影评分人数","电影主旨", "电影导演"]
    for i in range(7):
        worksheet.write(0, i, col[i])
    excel_list = []

    for i in range(0, 10):
        url = Url + str(i * 25)
        temp = Douban(path, url, getAgent())
        data = temp.getData()
        data_cont = data.read().decode("UTF-8")
        soup = BeautifulSoup(data_cont, "html.parser")
        for t in soup.find_all(class_="item"):
            s = str(t)
            link = re.findall(find_link, s)[0]
            img = re.findall(find_img, s)[0]
            title = re.findall(find_title, s)[0]
            rate = re.findall(find_rate, s)[0]
            people = re.findall(find_people, s)[0]
            file.write(f"电影名字{num}:{title}\n")
            file.write(f"电影链接:{link}\n")
            file.write(f"电影图片链接:{img}\n")
            file.write(f"电影评分:{rate}\n")
            file.write(f"电影评分人数:{people}\n")
            con = " "
            bd = " "
            try:
                con = re.findall(find_Con, s)[0]
            except IndexError:
                file.write(f"电影主旨:垃圾网站没有,熊二爬取不到!\n")
                con = "垃圾网站没有,熊二爬取不到!"
            else:
                file.write(f"电影主旨:{con}\n")
            try:
                bd = re.findall(find_Bd, s)[0]
                bd = bd.strip()
            except IndexError:
                file.write(f"电影导演:垃圾网站没有,熊二爬取不到!\n")
                bd="垃圾网站没有,熊二爬取不到!"
            else:
                file.write(f"电影导演:{bd}\n")

            excel_list.append(title)
            excel_list.append(link)
            excel_list.append(img)
            excel_list.append(rate)
            excel_list.append(people)
            excel_list.append(con)
            excel_list.append(bd)
            for j in range(7):
                worksheet.write(num, j, excel_list[j])
            workbook.save("./豆瓣Top250.xls")
            excel_list.clear()
            file.write("\n")
            num += 1
    file.close()
