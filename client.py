import socket

try:
    #connection verification
    s = socket.socket()#creating a socket
    s.connect((socket.gethostname(), 1234))#connect to particular IP address and port number
    print("Ready to message....!")
    
    while True:
        s = socket.socket()#creating a socket
        s.connect((socket.gethostname(), 1234))#connect to particular IP address and port number
        message=' '+(input("Enter message: "))
        s.send(bytes(message,'utf-8'))#send the data to server with encode
        full_msg = ''
        
        while True:
            msg = s.recv(1024) #receive data from server in 1024 byte stream
            if len(msg) <= 0:
                break
            full_msg += msg.decode('utf-8') #decoding and appending the received message
    
        if len(full_msg) > 0:
            print("Server Replay:",full_msg)
        
except:
    print("Connection aborted...!")

