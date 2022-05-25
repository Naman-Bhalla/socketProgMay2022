import socket
import threading
import time

def handleConnection(conn_socket, address):
    print(conn_socket)
    print(address)
    time.sleep(1)
    # conn_socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8080))
s.listen()
thread_list = []
all_cons = []

while True:
    conn_socket, address = s.accept()
    handleConnection(conn_socket, address)

    # thread = threading.Thread(target=handleConnection,
    #                           args=(conn_socket, address))
    # thread.start()
    # thread_list.append(thread)
    # all_cons.append(conn_socket)
    # current_thread_count = threading.active_count()
    # if current_thread_count == 200:
    #     print("Random")
    # print("Current active threads count = " + str(threading.active_count()))

# Server
# - Client sends a request
# - Server's OS Socket Receives it
# - let's say request is for IP 0.0.0.0 PORT 123
#     from IP 192.168.1.1 PORT 321
# OS checks out of all the sockets it has, is there a
# socket for that lAddr and rADDre
# If yes, send data to that socket
# If no socket with the same lAddr and rAddr, OS sees
# if there is a socket with that lAddre

#