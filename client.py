import socket

class UDPClient:
    def __init__(self, udp_ip, udp_port):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.message = b'Hello NetSense !!!!'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self):
        print("UDP target IP: %s" % self.udp_ip)
        print("UDP target port: %s" % self.udp_port)
        print("message: %s" % self.message)
        self.sock.sendto(self.message, (self.udp_ip, self.udp_port))

# Example usage:
#udp_client = UDPClient("192.168.178.34", 5005)
#udp_client.send_message()