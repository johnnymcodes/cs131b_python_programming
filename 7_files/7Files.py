import time
import sys
cmarg = sys.argv[1:] #returns a list of cmd arguments

query = cmarg[0]
try:
    print('Warning! Does not filter explicit language')
    time.sleep(2)
    fhand = open('/users/abrick/resources/english')
    for line in fhand:
        line = line.strip() #remove leading and ending white space
        # print(stripped)
        if line.startswith(query):
            print(line)
except:
    print( 'File Not Found!')