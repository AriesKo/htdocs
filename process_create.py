#!C:\Users\SANGIL\AppData\Local\Programs\Python\Python36\python.exe

import cgi
form = cgi.FieldStorage()
title = form.getvalue('title')
descrption = form.getvalue('descrption')

f_create_file = open('data/'+title, 'w')
f_create_file.write(descrption)
f_create_file.close()

print("Location: index.py?id="+title) # Redirectoin
print()
