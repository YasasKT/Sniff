import argparse
import logging
from scapy.all import sniff
from .analysis import full_analysis

def packet_handler(packet):
    full_analysis(packet)
    logging.info(packet.summary())


def main():
    parser = argparse.ArgumentParser(description='Simple Packet Sniffer')
    parser.add_argument('-i', '--interface', required=True, help='Network interface to capture packets on')
    parser.add_argument('-c', '--count', type=int, default=0, help='Number of packets to capture (0 for unlimited)')
    parser.add_argument('-f', '--filter', default='', help='BPF filter to apply')
    args = parser.parse_args()

    logging.basicConfig(filename='packets.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    print(f"Sniffing on interface {args.interface} with filter '{args.filter}'...")
    sniff(iface=args.interface, count=args.filter, prn=packet_handler)

if __name__ == '__main__':
    main()