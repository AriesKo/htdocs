#!C:\Users\SANGIL\AppData\Local\Programs\Python\Python36\python.exe

import cgi, os
form = cgi.FieldStorage()
pageId = form.getvalue('pageId')

os.remove('data/'+pageId)

print("Location: index.py") # Redirectoin
print()