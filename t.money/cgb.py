import requests
from bs4 import BeautifulSoup
import xlwt

response = requests.get('http://www.cgbchina.com.cn/Channel/16684283?nav=2?nav=2') # 广发理财

soup = BeautifulSoup(response.content, features="html.parser") # 转换为bs4格式

list = [ [0]*22 for i in range(20)] # 二维数组
k = 0

for i in soup.find_all('tr', class_="bg2"): # 定位到一行
    k2 = 0
    for j in i.strings:
        if len(j) != 1:
            list[k][k2] = str(j)
            k2 += 1
    k += 1

book = xlwt.Workbook(encoding='utf-8', style_compression=0) # excel支持
sheet = book.add_sheet('test', cell_overwrite_ok=True) # excel支持，其中test为tab名

for i in range(0, 12):
    for j in range(0, 22):
        sheet.write(i, j, list[i][j])

book.save(r'test.xls')
# book.save(r'/users/zach/PycharmProjects/t/venv/test.xls')