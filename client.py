import socket

def main():
    client_socket=socket.socket()
    client_socket.connect(('localhost', 5000))
    print("Client Connected")
    
    client_msg="Hello"
    client_socket.send(client_msg.encode())
    print("Client says:", client_msg)
    
    server_response=client_socket.recv(1024).decode()
    print("Server says:", server_response)
    
    client_socket.close()
    print("Connection Closed")
    
if __name__=="__main__":
    main()