import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
n=1
url =  "http://python-data.dr-chuck.net/comments_283399.html"

count= int(input('Enter count'))+1
pos=int(input('Enter position'))
new=url
while n<count:
    if new == url:
        html = urllib.request.urlopen(url, context=ctx).read()
        print('Retrieving', url)
    html = urllib.request.urlopen(new, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    my_tags=tags[pos-1]
    new=my_tags.get('href', None)
    print('Retrieving' , new)
    n=n+1
