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
