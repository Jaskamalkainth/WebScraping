import urllib2
import codecs
from bs4 import BeautifulSoup

url  = "http://codeforces.com/ratings"
page = urllib2.urlopen(url)


soup = BeautifulSoup(page.read())

row1 = soup.find_all('a' ,class_ = "rated-user user-legendary" )
row2 = soup.find_all('a' ,class_ = "rated-user user-red" )
row3 = soup.find_all('a' ,class_ = "rated-user user-orange" )


f = codecs.open ( "codeforces_top_100.txt " , "w" , "utf-8" )

for row in row1:
    f.write( row['title'] + "\n")
for row in row2:
    f.write( row['title'] + "\n")
for row in row3:
    f.write( row['title'] + "\n")

f.close()


