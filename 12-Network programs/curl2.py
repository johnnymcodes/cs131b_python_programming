#In order to avoid runnind out of memory for large media files
#retrieve the data in blocks or (buffers)
#then write each block to your disk before retrieving the next block.
#this way the program can read andy size file without using up all of the memory on the computer

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied')
fhand.close()
