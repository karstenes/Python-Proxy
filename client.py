import socket, webbrowser, os
inputt=raw_input("Webpage: ")
if inputt=="":
    inputt="http://google.com/"
server=raw_input("web server (ip:port): ")
if server=="":
    #server="108.41.183.93:443"
    server="localhost:443"
server=(server[:server.index(':')], int(server[server.index(':')+1:]))
print server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(server) 
s.send(inputt)
size=int(s.recv(1024))
ff=s.recv(10)
print "receiving "+ff+" file with size "+str(size)
data=s.recv(size)
print data
s.close()
with open("temp."+ff, 'wb') as temp:
    temp.write(data)
    temp.close()
os.system('"C:\Program Files\Internet Explorer\iexplore.exe" file://'+os.getcwd()+'/temp.'+ff)

