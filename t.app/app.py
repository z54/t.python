#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
ikey = "eWeLink"
url = "https://play.google.com/store/search?q=" + ikey
# url = "http://www.baidu.com/s?ie=UTF-8&wd=" + ikey
# url = "https://www.google.com/search?&q=" + ikey +"&oq=" + ikey
# url = "https://www.google.com/"
print(url)
# response = requests.get(url)
response = requests.get(url)
# proxy = {
#     "http": "http://127.0.0.1:1080",
#     "https": "https://127.0.0.1:1080"
# }
# response = requests.get("https://www.google.com.hk", proxies=proxy)

soup = BeautifulSoup(response.content, features="html.parser")
# print(soup.prettify())
# print(soup.html.prettify().encode('utf-8'))
# print(soup.div.prettify().encode('utf-8'))

# for i in soup.find_all('div', title=ikey):
#     print(i)
#     print(i.string)

for i in soup.find('div', title=ikey):
    print(i)
    print(i.string.encode('utf-8'))