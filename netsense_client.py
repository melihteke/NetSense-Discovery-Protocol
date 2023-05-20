import socket
import struct

class NetSenseFrameTLV:
    def __init__(self, tlv_type, tlv_length, tlv_value):
        self.tlv_type = tlv_type
        self.tlv_length = tlv_length
        self.tlv_value = tlv_value

    def get_tlv(self):
        tlv = {
            "tlv_type": self.tlv_type,
            "tlv_length": self.tlv_length,
            "tlv_value": self.tlv_value
        }
        return tlv

class NetSenseEthernetFrame:
    def __init__(self, source_mac, destination_mac):
        self.source_mac = source_mac
        self.destination_mac = destination_mac
        self.ethertype = 0x88CC
        self.tlvs = []

    def add_tlv(self, tlv):
        self.tlvs.append(tlv)

    def get_frame(self):
        frame = {
            "source_mac": self.source_mac,
            "destination_mac": self.destination_mac,
            "ethertype": self.ethertype,
            "tlvs": []
        }

        for tlv in self.tlvs:
            frame["tlvs"].append(tlv.get_tlv())

        return frame


# Create the Ethernet frame
ethernet_frame = NetSenseEthernetFrame("bc:d0:74:36:2b:a4", "1a:51:f5:a9:c8:fe")  # Use broadcast address as destination

# Add TLVs
chassis_id_tlv = NetSenseFrameTLV(1, 8, "Router01")
port_id_tlv = NetSenseFrameTLV(2, 4, "Eth1")
ttl_tlv = NetSenseFrameTLV(3, 3, 120)
ethernet_frame.add_tlv(chassis_id_tlv)
ethernet_frame.add_tlv(port_id_tlv)
ethernet_frame.add_tlv(ttl_tlv)

# Get the frame data
frame_data = ethernet_frame.get_frame()

# Pack the frame data into binary format
source_mac_bytes = bytes.fromhex(frame_data['source_mac'].replace(':', ''))
destination_mac_bytes = bytes.fromhex(frame_data['destination_mac'].replace(':', ''))
ethertype_bytes = struct.pack('!H', frame_data['ethertype'])

binary_frame_data = source_mac_bytes + destination_mac_bytes + ethertype_bytes

for tlv in frame_data['tlvs']:
    tlv_type_bytes = struct.pack('!B', tlv['tlv_type'])
    tlv_length_bytes = struct.pack('!H', tlv['tlv_length'])
    tlv_value_bytes = str(tlv['tlv_value']).encode()  # Convert to string and then encode
    binary_frame_data += tlv_type_bytes + tlv_length_bytes + tlv_value_bytes


# Send the binary frame data to broadcast
server_address = ('192.168.178.34', 5005)  # Use the broadcast address and appropriate port

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    client_socket.sendto(binary_frame_data, server_address)

print('Frame sent to broadcast.')
