import socket
import urllib.parse as up
import urllib.request as ur
#find my ip address

try: 
    host = socket.gethostname()
    add = socket.gethostbyname(host)
    print(add)
except Exception as e:
    print("Failed to get host name.")


try:
    host = 'JEEBAN'
    addr  = socket.gethostbyname(host)
    print(addr)
except socket.gaierror:
    print("Web site Does not exists")

#find different parts of a url

url = 'https://www.javatpoint.com/gmail-api-in-python'

tpl = up.urlparse(url)
print(tpl)
print(tpl.port)
print(tpl.geturl())

#reading the source code of a webpage
url = "https://www.w3schools.com/python/"

file = ur.urlopen(url)
content = file.read()
f = open('myfile.html','wb')
f.write(content)

#download an image
url = "https://img.freepik.com/premium-vector/santa-hat-is-black-background_975374-4849.jpg"
download = ur.urlretrieve(url,'myimage.png')