from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())  # get_text 会把超链接、段落和标签都清除掉，只剩下一串不带标签的文字

print(bs.findAll(string='the prince'))  # text 参数已经废弃，使用string替换
print(bs.div)
