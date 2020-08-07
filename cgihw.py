#!/usr/local/bin/python3--
print("Content-type:text/html\n")
import cgi
form = cgi.FieldStorage()
print ( form.getvalue("name") ) 