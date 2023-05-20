import socket

# Server configuration
server_address = ('192.168.178.34', 5005)  # Server IP address and port
binary_frame_data = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\x01\x23\x45\x67\x88\xCC\x01\x07Switch-A\x02\x08GigabitEthernet1/1\x03\x02\x01\x20'

try:
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Send the binary frame data to the server
    client_socket.sendall(binary_frame_data)

    # Close the connection
    client_socket.close()

except Exception as e:
    print('Error:', e)