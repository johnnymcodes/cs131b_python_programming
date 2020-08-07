# urllib to read the page and then use BeautifulSoup to extract the href attributes from the anchor(a) tagsself.
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieves all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
