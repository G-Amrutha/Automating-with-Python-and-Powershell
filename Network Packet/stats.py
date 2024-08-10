from scapy.all import sniff, IP
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

interface = "Wi-Fi"

# Parameters
NUM_PACKETS = 6000  # Number of packets to sniff

def handle_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        timestamp = packet.time
        
        src_ips.append(src_ip)
        dst_ips.append(dst_ip)
        timestamps.append(timestamp)

def plot_frequencies(data, title):
    counter = Counter(data)
    plt.figure(figsize=(10, 5))
    plt.bar(counter.keys(), counter.values())
    plt.title(title)
    plt.xlabel("IP Addresses")  # X-axis label
    plt.ylabel("Frequency")     # Y-axis label
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    plt.show()

# Lists to store data
src_ips = []
dst_ips = []
timestamps = []

# Start packet sniffing
packets = sniff(iface='Wi-Fi', count=NUM_PACKETS, filter="ip", prn=handle_packet)

# Print total number of packets captured
print(f"Total packets captured: {len(src_ips)}")

# Display the frequencies of source and destination IP addresses
print("Frequencies of Source IPs:")
print(Counter(src_ips))
print("Frequencies of Destination IPs:")
print(Counter(dst_ips))

# Plotting
plot_frequencies(src_ips, "Frequencies of Source IP Addresses")
plot_frequencies(dst_ips, "Frequencies of Destination IP Addresses")

# Extra credit: plot packet frequencies over time
if timestamps:
    plt.figure(figsize=(10, 5))
    plt.hist(timestamps, bins=np.arange(min(timestamps), max(timestamps) + 10, 10), alpha=0.75, color='green')
    plt.title("Packet Timestamps Distribution")
    plt.xlabel("Time (Since First Captured Packet)")
    plt.ylabel("Number of Packets")
    plt.show()
