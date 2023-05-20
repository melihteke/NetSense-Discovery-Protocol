import socket
import struct

# Server configuration
host = '0.0.0.0'  # Listen on all available interfaces
port = 5005

# Create a socket and bind it to the server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

# Listen for incoming connections
print('Server listening on {}:{}'.format(host, port))

while True:
    # Receive the Ethernet frame data
    binary_frame_data, client_address = server_socket.recvfrom(4096)
    print('Received frame from {}:{}'.format(client_address[0], client_address[1]))

    # Unpack the Ethernet frame data
    source_mac_bytes = binary_frame_data[:6]
    destination_mac_bytes = binary_frame_data[6:12]
    ethertype_bytes = binary_frame_data[12:14]

    source_mac = ':'.join(['{:02x}'.format(b) for b in source_mac_bytes])
    destination_mac = ':'.join(['{:02x}'.format(b) for b in destination_mac_bytes])
    ethertype = struct.unpack('!H', ethertype_bytes)[0]

    # Process the TLVs (if any)
# Process the TLVs (if any)
    tlvs = []
    tlv_data = binary_frame_data[14:]
    while len(tlv_data) >= 4:
        tlv_type = struct.unpack('!B', tlv_data[:1])[0]
        tlv_length = struct.unpack('!H', tlv_data[1:3])[0] & 0x7FFF  # Extract length using lower 15 bits
        tlv_value = tlv_data[3:3+tlv_length].decode()
        tlvs.append({
            'tlv_type': tlv_type,
            'tlv_length': tlv_length,
            'tlv_value': tlv_value
        })
        tlv_data = tlv_data[3+tlv_length:]


    # Print the received frame information
    print('Source MAC:', source_mac)
    print('Destination MAC:', destination_mac)
    print('EtherType:', ethertype)
    print('TLVs:')
    for tlv in tlvs:
        print('  Type:', tlv['tlv_type'])
        print('  Length:', tlv['tlv_length'])
        print('  Value:', tlv['tlv_value'])
        print()

server_socket.close()