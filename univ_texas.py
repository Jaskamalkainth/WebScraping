

import urllib2
import codecs
from  bs4 import BeautifulSoup

#opening the URL

url = "http://www.utexas.edu/world/univ/alpha/"
page = urllib2.urlopen(url)

#creating the soup

soup = BeautifulSoup(page.read())

universities = soup.find_all('a' , class_ = "institution")

#iterate over all the universities


f = codecs.open("data.txt","w","utf-8")

for u in universities:
    f.write(  u['href'] + '  ,  ' + u.string + "\n")

f.close()
