import socket

print('Please enter a URL')
urlstr = raw_input().strip()
words = urlstr.split('/')
host = words[1]
print(host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#makes a connection to port 80 on the server www.py4e.com
mysock.connect(('data.pr4e.org', 80))
#since our program is playing the role of the 'web browser', the HTTP protocol says we must send the GET command followed by a blank line.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
#once we send that blank line. write a loop that receives data in 512-character chunks from the socket and prits the data out until there is no more data to read i.e. recv() returns an empty string.
while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()

# equivalent code using urllib
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
