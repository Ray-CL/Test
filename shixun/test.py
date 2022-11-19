import urllib.request

url = "http://www.baidu.com"
res = urllib.request.urlopen(url)
print(res.read())
