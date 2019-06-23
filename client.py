import socket
s=socket.socket()
print("socket created")

port=80
s.bind((' ',port))
print("socket binded to %s"%port)
s.listen(5)
print("socket is listening")

while True:
    c,addr=s.accept()
    print("got connection from",addr)
    c.send('tnx for connection')
    c.close()
