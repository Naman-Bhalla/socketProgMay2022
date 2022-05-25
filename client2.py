import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(("localhost", 8080))
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(("localhost", 8080))

s2.sendall(b"status: OK I am going to home")
s2.sendall(b"hello")
s1.sendall(b"status: OK I am going to home")
s1.sendall(b"hello")