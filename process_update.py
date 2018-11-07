#!C:\Users\SANGIL\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form.getvalue('id')
title = form.getvalue('title')
descrption = form.getvalue('descrption')

f_update_file = open('data/'+ pageId, 'w')
f_update_file.write(descrption)
f_update_file.close()

os.rename('data/'+pageId, 'data/'+title)

print("Location: index.py?id="+title) # Redirectoin
print()