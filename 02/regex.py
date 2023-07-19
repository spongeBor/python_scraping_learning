from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    # print(image['src'])
    print(image.attrs)

attr2 = bs.findAll(lambda tag: len(tag.attrs) == 2)
for attr in attr2:
    print('\n', attr, '\n')
