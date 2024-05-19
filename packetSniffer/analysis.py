from scapy.all import IP, TCP, UDP, ICMP, DNS, DNSQR, TLS, Raw, Ether

def basic_analysis(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")

    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        print(f"Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")


def http_analysis(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors='ignore')
        if payload.startswith(('GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'CONNECT')):
            print(f"HTTP Request: {payload.splitlines()[0]}")
            print(f"HTTP Headers: {payload}")


def dns_analysis(packet):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        dns_layer = packet.getlayer(DNS)
        dns_query = dns_layer.qd
        print(f"DNS Query for {dns_query.qname.decode()} of type {dns_query.qtype}")


def icmp_analysis(packet):
    if packet.haslayer(ICMP):
        icmp_layer = packet.getlayer(ICMP)
        print(f"ICMP Type: {icmp_layer.type}, Code: {icmp_layer.code}")


def packet_size_analysis(packet):
    print(f"Packet Size: {len(packet)} bytes")


def mac_address_analysis(packet):
    if packet.haslayer(Ether):
        ether_layer = packet.getlayer(Ether)
        print(f"Source MAC: {ether_layer.src}, Destination MAC: {ether_layer.dst}")


def ssl_tls_analysis(packet):
    if packet.haslayer(TLS):
        tls_layer = packet.getlayer(TLS)
        print(f"SSL/TLS Version: {tls_layer.version}, Cipher Suite: {tls_layer.cipher_suite}")


def full_analysis(packet):
    basic_analysis(packet)
    http_analysis(packet)
    dns_analysis(packet)
    icmp_analysis(packet)
    packet_size_analysis(packet)
    mac_address_analysis(packet)
    ssl_tls_analysis(packet)