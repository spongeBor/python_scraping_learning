
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

pages = set()


def getLinks(pageUrl):
    pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.getText())
        print(bs.find(id='mw-content-text').findAll('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('页面缺少一些属性，不用担心!')
    except IndexError:
        print('out of range')

    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
