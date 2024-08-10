from scapy.all import *

interface="Wi-Fi"

def print_packet(packet):
      #packet.show()
      ip_layer=packet.getlayer(IP);
      print("[!]New Packet: {src}->{dst} using {proto}".format(src=ip_layer.src,dst=ip_layer.dst, proto=ip_layer.proto));

print("[*] Start sniffing...")
sniff(count=10,iface=interface, filter="ip",prn=print_packet)
print("[*] Stop sniffing")







