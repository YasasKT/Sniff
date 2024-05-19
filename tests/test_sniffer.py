import unittest
from scapy.all import Ether, IP, TCP
from packetSniffer.sniffer import packet_handler

class TestPacketSniffer(unittest.TestCase):
    def test_packet_handler(self):
        packet = Ether()/IP(src="192.168.1.1", dst="192.168.1.2")/TCP(sport=12345, dport=80)
        packet_handler(packet)

if __name__ == '__main__':
    unittest.main()