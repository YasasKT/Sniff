import unittest
from scapy.all import Ether, IP, TCP
from packetSniffer.analysis import analyze_packet

class TestPacketAnalysis(unittest.TestCase):
    
    def test_analyze_packet(self):
        packet = Ether()/IP(src="192.168.1.1", dst="192.168.1.2")/TCP(sport=12345, dport=80)
        analyze_packet(packet)

if __name__ == '__main__':
    unittest.main()