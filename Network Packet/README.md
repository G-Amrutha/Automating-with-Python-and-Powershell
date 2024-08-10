# Network Packet Statistics Script

## Overview

The `stats.py` script is designed to capture and analyze network packets, focusing on IP traffic over a specified network interface. It provides insights into the frequencies of source and destination IP addresses and visualizes packet data distribution over time.

## Requirements

- Python 3.x
- Scapy library
- Matplotlib library
- NumPy library

To install the required Python libraries, run:
```bash
pip install scapy matplotlib numpy
```

## Usage

### Description

The script captures a specified number of network packets on a given interface and analyzes the IP traffic. It plots the frequencies of source and destination IP addresses and the distribution of packet timestamps.

### How to run

1. Open the script and set the `interface` variable to the name of your network interface (e.g., `eth0`, `Wi-Fi`, etc.).
2. Set the `NUM_PACKETS` variable to the number of packets you want to capture (e.g., 6000).
3. Run the script:

```bash
python3 stats.py
```

### Output

- **Frequencies of Source and Destination IPs:** The script prints the frequency of each source and destination IP address in the captured packets.
- **Plots:**
  - **Source IP Frequencies:** A bar chart showing the frequency of each source IP address.
  - **Destination IP Frequencies:** A bar chart showing the frequency of each destination IP address.
  - **Packet Timestamps Distribution:** A histogram showing the distribution of packet arrival times.

### Notes

- Ensure you have the necessary permissions to capture network packets on your system.
- The script uses the `Wi-Fi` interface by default; adjust it to match your network interface.
- Modify `NUM_PACKETS` to control the number of packets the script captures and analyzes.
