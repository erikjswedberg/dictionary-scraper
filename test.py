# import urllib2
# url='https://github.com/johnpapa?tab=followers'
# content = urllib2.urlopen(url).read()
# soup = BeautifulSoup(content, 'html.parser')
# for lt in soup.find_all("a",class_="url"):
#     if lt.get("href"):
#         si=lt.get("href")
#         print si
# for item in soup.find_all("a",class_="d-inline-block no-underline mb-1"):
#     url1=item.get("href")
#     url1='https://github.com'+url1+'?tab=followers'
#     print url1
#     content = urllib2.urlopen(url1).read()
#     soup1 = BeautifulSoup(content, 'html.parser')
#     for lt in soup1.find_all("a",class_="url"):
#         if lt.get("href"):
#             si=lt.get("href")
#             print si
#     for item in soup1.find_all("a",class_="d-inline-block no-underline mb-1"):
#             url1=item.get("href")
#             url1='https://github.com'+url1+'?tab=followers'
#             print url1


from bs4 import BeautifulSoup
import  requests
word = "democracy"
url = 'https://www.google.co.in/search?q=define%20' + word + '#cns=1'
response = requests.get(url, headers={"user-agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0"})
html = response.content
final_soup = BeautifulSoup(html,"html5lib")
everyThing = final_soup.select("div._Jig")
print everyThing
for line in everyThing:
    print("-",line.text)