import socket, urllib, time, os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 443))
s.listen(5)
while True:
    client, address = s.accept()
    print "Client connected, receiving data.."
    data = client.recv(1024)
    if data:
        print "received "+data
        f = urllib.urlretrieve(data, "temp.txt")
        csize = os.stat("temp.txt").st_size
        print csize
        print csize/4096
        print csize % 4096
        if csize % 4096 !=0:
            csize=csize- csize % 4094
            csize=csize+4096
        print csize
        content = open("temp.txt", 'rb').read(csize)
        client.send(str(csize))
        if data[len(data)-5:]==".html" or data[len(data)-4:]==".htm" or "." not in data[len(data)-5:] or data.endswith("/"):
            print "sending back html"
            client.send("html")
        elif data[len(data)-5]=="." or data[len(data)-4]=="." or data[len(data)-3]==".":
            print "sending back "+data[data.rfind(".")+1:]
            client.send(data[data.rfind(".")+1:])
        client.send(content)
    client.close()
