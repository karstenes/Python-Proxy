import socket, webbrowser, os
inputt=raw_input("Webpage: ")
if inputt=="":
    inputt="http://google.com/"
server=raw_input("web server (ip:port): ")
if server=="":
    server="127.0.0.1:1234"
server=(server[:server.index(':')], int(server[server.index(':')+1:]))
print server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(server) 
s.send(inputt)
data=s.recv(102400)
s.close()
with open("temp.html", 'w') as temp:
    temp.write(data)
    temp.close()
os.system('"C:\Program Files\Internet Explorer\iexplore.exe" file://'+os.getcwd()+'/temp.html')

