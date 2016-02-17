import urllib.request
from bs4 import BeautifulSoup
import random

r = random.randrange(1, 1431045)
movie_url = 'http://www.imdb.com/title/tt' + str(r) + '/keywords'
print (movie_url)
page = urllib.request.urlopen(movie_url)
soup = BeautifulSoup(page.read(), "lxml")
keywords = soup.find_all(attrs={"data-item-keyword":True})
for i in range (0, len(keywords)):
	print (keywords[i]['data-item-keyword'])