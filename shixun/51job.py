# -*- coding=utf-8 -*-
# Time:2022/10/1 18:34
# Author:Ray
# File:51job.py
# Software:PyCharm
import re
import urllib.request
import random
import json

def getData(url, head):
    req = urllib.request.Request(url=url, headers=head, method="POST")
    data = urllib.request.urlopen(req)
    return data


def getheader():
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
                  "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"]
    headers = {"User-Agent": random.choice(user_agent)}
    return headers


Url = "https://search.51job.com/list/000000,000000,0124,00,9,99,+,2,"
find_data = re.compile(r'"engine_jds":(.*?),"jobid_count"', re.S)
for i in range(1):
    url = Url + str(i) + ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    data_code = getData(url, getheader())
    temp = data_code.read()

    # file = open("render.html", "w", encoding="gbk")
    # file.write(temp)
    print(temp)
    # print(type(file.read()))
    # data = re.findall(find_data, file.read())[0]
    # data = json.loads(data)
    # for i in data:
    #     print(i["job_href"])
    #     print(i["job_name"])
    #     print(i["company_href"])
    #     print(i["company_name"])
    #     print(i["providesalary_text"])
    #     print(i["workarea_text"])
    #     print(i["issuedate"])
    #     print(i["jobwelf"])
    #     print(i["companysize_text"])
    #     print()
