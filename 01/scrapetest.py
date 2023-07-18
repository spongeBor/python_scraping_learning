from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://pythonscraping.com/pages/page1.html")
# bs = BeautifulSoup(html.read(), "html.parser")
# bs = BeautifulSoup(html.read(), "lxml")
# bs = BeautifulSoup(html.read(), "html5lib")


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print('Title could not be found')
else:
  print(title)
