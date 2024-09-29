
import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
a=s.recv(1204)
print(a.decode()+"i am a client one")
s.close()

