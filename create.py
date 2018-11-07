#!C:\Users\SANGIL\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html") # html markup follows
print()

import cgi,cgitb
import os

def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href = index.py?id={name}>{name}</a></li>'.format(name=item)
    
    return listStr

cgitb.enable() #for debugging 
form = cgi.FieldStorage()

if 'id' in form:
    pageId = form.getvalue('id')
    description = open('data/'+pageId,'r').read()
    img = "<img src = 'image/PI_{name}.png' width = 100%>".format(name = pageId)
else:
    pageId = "Welcome"
    description = "Welcome to the Image Compression Test project"
    img = "<img src = 'image/spacex.jpg' width = 100%>"
 
htmlFormat = '''<!doctype html>
<html>
    <head>
        <title>WEB1 - html</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/css/my_style.css">
    </head>
    
    <body>
        <h1><a href = "index.py">Image Compression Unit Test</a></h1> 
        <div id="grid">
            <ol>
                {listStr}
            </ol>
            <div>
                <h2>{title}</h2>
                <p>{desc}</p>
                <form action="process_create.py" method="post">
                    <p><input type="text" name="title" placeholder="title"></p>
                    <p><textarea rows="4" name="descrption" placeholder="descrption"></textarea></p>
                    <p><input type="submit"></p>
                </form>
                <p>{img}</p>
            </div>
        </div>
    </body>
</html>
'''
#print(htmlFormat)
print(htmlFormat.format(title=pageId, desc = description, listStr = getList(), img = img))
