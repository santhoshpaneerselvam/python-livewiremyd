
import socket
s=socket.socket()
host=socket.gethostname()
print(host)

port=12345
s.bind((host,port))
s.listen(5)

while True:
    c,addr=s.accept()
    print('got connection from ',addr)
    s1="thank you for connecting"
    c.send(s1.encode())
    c.close()
