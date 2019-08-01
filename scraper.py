import sys
import urllib
import urllib2
from bs4 import BeautifulSoup


inputFile = 'shortwords.txt'
outputFile = 'out.txt'
limit = 1
shouldGetRootsPicture = False
rootPictureFolder = 'roots'

args = {}
for index, arg in enumerate(sys.argv):
  if(arg == '-i'):
    inputFile = sys.argv[index+1]
  if (arg == '-o'):
    outputFile = sys.argv[index+1]
  if (arg == '-l'):
    limit = int(sys.argv[index+1])


baseUrl = "https://google.com/search?q=define+"
headers = urllib.urlencode({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
})

with open(inputFile, 'r') as fs:
  while limit > 0:
    nextWord = fs.readline()
    # print nextWord
    # print baseUrl + nextWord

    opener = urllib2.build_opener()
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')]
    # opener.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36')]


    page = opener.open(baseUrl + nextWord)
    html = page.read()
    page.close()

    soup = BeautifulSoup(html, 'html5lib')
    # print soup

    print soup.find('g-img')

    # print soup.find_all("div", class_="lr_dct_sf_h").i.span
    # print soup.find("div", class="lr_dct_sf_h")
    # type = soup.find(id="search")
    # print type



    limit = limit - 1

