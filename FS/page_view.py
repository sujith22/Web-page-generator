#!/usr/bin/python3
print("Content-type: text/html")
print()
print("<!DOCTYPE html> <html> <head>")
print('''<title>company.txt</title> <link href="https://bootswatch.com/4/cyborg/bootstrap.min.css" rel="stylesheet">
<style>
p{
    font-size:22px;
    line-height:1.5em;
}</style>
</head>''')
print('<body class = "container bg-dark text-white">')
f = open("company.txt")
print("<br>")
print('''<h3 class='text-center text-primary display-3'> Delimiter for fields is '|' <br> Delimiter for records is '###'</h3>''')
for lines in f:
    lines=lines.rstrip()
    print("<p>"+lines+"</p>")
print('</body> </html>')



