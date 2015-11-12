import socket, urllib2
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(5)
while True:
    client, address = s.accept()
    print "Client connected, receiving data.."
    data = client.recv(1024)
    if data:
        print "received "+data
        f = urllib2.urlopen(data)
        content = f.read()
        print "sending back html"
        client.send(content)
    client.close()
