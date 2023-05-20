import socket
class UDPServer:
    def __init__(self, udp_ip, udp_port, buffer_size=1024):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.udp_ip, self.udp_port))
    def receive_message(self):
        data, addr = self.sock.recvfrom(self.buffer_size)
        print("received message: %s" % data)

# Example usage:
udp_server = UDPServer("192.168.178.34", 5005)
while True:
    udp_server.receive_message()

