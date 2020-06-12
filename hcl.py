from http.server import HTTPServer, CGIHTTPRequestHandler
import webbrowser, pathlib

'''
HCLite Fondation.
Created by Lamer3011
Version 0.01
'''

# Проверка на наличии файла
try:
    f = open('index.html')
    print("File is found!\nRuning server")
    f.close()
except IOError:
    print('File will be created')
    # Создание файла
    htmlfile = open("index.html", "w")
    htmlfile.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Hello HCLServer!</h1>
</body>
</html>
""")
    htmlfile.close()
##################
# Сам сервер
webbrowser.open('http://localhost:8080/')
print('**','localhost:8080', '**')
print('EVENTS:')
server_data = ('localhost', 8080)
server = HTTPServer(server_data,CGIHTTPRequestHandler)
server.serve_forever()