# output of cgi script consists of two sections.
# The first section contains a number of headers, telling the client what kind of data is following.
print("Content-Type: text/html")
print()
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first cgi script<H1>")
print("Hello, world")

#using CGi model
import cgi

#when writing a new script, consider adding these linesL
#this activated a special exception handler that will display detailed reports

import cgitb
cgitb.enable()
#can save reports to file like This
#cgitb.enable(display=0, logdir="path/to/logdir")


#to get submitted form data use fieldStorage class
form = cgi.FieldStorage()
#to keep empty values provide a true value for the optional keep_blank_values
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")

print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)
