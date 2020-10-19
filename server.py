import socket

try:
    
    s = socket.socket()  #creating a socket
    s.bind((socket.gethostname(), 1234)) #binding the socket with a port number and IP address
    s.listen(5) #maximum number of acceptable connections
    full_msg=''
    print("Waiting for the Connections...!")
    clientsocket, address = s.accept() #accepting the client
    claint_replay=clientsocket.recv(1024).decode()  #receive a data from client and decode it
    print(f"Connection from IP address {address} has been established.")
    clientsocket.close() #close the socket

    while True:
        clientsocket, address = s.accept() #accept the client
        claint_replay=clientsocket.recv(1024).decode() #receive a data from client in 1024 byte stream and decode the data
        print("Client replay:",claint_replay)
        message=' '+(input("Enter message: "))
        clientsocket.send(bytes(message,"utf-8"))# send the data to client
        clientsocket.close() #close the socket
except:
    print("Connection aborted..!")
