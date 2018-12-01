from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页

html = urlopen('https://www.lagou.com/')
bsObj = BeautifulSoup(html, 'html.parser')

t1 = bsObj.find_all('a')

f = open('test.txt', 'w')
for t2 in t1:
    t3 = t2.get('href')
    t4 = t2.text
    if t4 is not None and len(t4) > 4 and t3 is not None and t3[:4] == 'http':
        f.write(t4.strip().replace("\n", "") + " " + t3 + "\n")
f.close()
