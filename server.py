import socket

def main():
    server_socket=socket.socket()
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("Connecting....")
    
    client_socket, _=server_socket.accept()
    print("Client Connected")
    
    client_msg=client_socket.recv(1024).decode()
    print("Client sends:", client_msg)
    
    server_msg="Good to see you"
    client_socket.send(server_msg.encode())
    print("Server to client:", server_msg)
    
    server_socket.close()
    client_socket.close()
    print("Connection closed")
    
if __name__=="__main__":
    main()
    