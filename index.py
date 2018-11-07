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
    create_link = ""
    update_link = "<a href = 'update.py?id={}'>update</a>".format(pageId)
    delete_action = '''
        <form action="process_delete.py" method = "post">
            <input type = "hidden" name = "pageId" value ="{}">
            <input type = "submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = "Welcome"
    description = "Welcome to the Image Compression Test project"
    img = "<img src = 'image/spacex.jpg' width = 100%>"
    create_link = "<a href = 'create.py'>create</a>"
    update_link = ""
    delete_action = ""

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
                {create_link}
                {update_link}
                {delete_action}
                <p>{img}</p>
            </div>
        </div>
    </body>
</html>
'''
#print(htmlFormat)
print(htmlFormat.format(title=pageId, desc = description, listStr = getList(), img = img, create_link=create_link,update_link=update_link,delete_action=delete_action))
