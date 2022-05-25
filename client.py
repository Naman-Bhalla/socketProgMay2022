import socket
import threading
# Socket s = new Socket()
# Type of IP -> ipv4 (AF_INET), ipv6
# Type of Transport Layer -> UDP or TCP

# AF -> Address Family

def create_connection(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    data = str(i) + " status: OK I am going to home"

    s.sendall(data)

for i in range(500):
    t = threading.Thread(target=create_connection, args=i)
    t.start()
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(("localhost", 8080))
    #
    # s.sendall(b"status: OK I am going to home")
# s.send("I am goinng to my home") -> 4
# s.send(" goinng to my home") -> 6
# s.se

# data = s.recv(1024) # return type of this will be byte[]
# print(data)

s.close()
