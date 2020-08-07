import urllib.request, urllib.parse, urllib.errors

#reads all the data in at once accross the network and stores it in the variable img
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
#opens the file cover.jpg and writes the data out to disk
fhand = open('cover.jpg', 'wb')
fhand.write(img)
fhand.close()
