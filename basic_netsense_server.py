import socket

# Server configuration
host = '192.168.178.34'  # Server IP address
port = 5005

# Create a socket and bind it to the server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print('Server listening on {}:{}'.format(host, port))

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

    # Receive the data from the client
    received_data = client_socket.recv(1024)
    print('Received data:', received_data)

    # Close the client connection
    client_socket.close()