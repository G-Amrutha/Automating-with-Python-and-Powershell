#!/usr/bin/env python3
# Script Name: services_report.py
# Purpose: Generate a report of open network ports and their associated services and functions.

import os
# Import os module to interact with the operating system.

import socket
# Import socket module for network-related functions such as service name lookup.

import pandas as pd
# Import pandas module for data manipulation and analysis.

import subprocess
# Import subprocess module to run system commands and capture their output.

# Execute 'ss -tuln' command to list all listening TCP and UDP sockets and capture the output.
result = subprocess.run(['ss', '-tuln'], stdout=subprocess.PIPE)

# Decode the command output from bytes to a string format for easier processing.
output = result.stdout.decode()

# Initialize an empty list to store information about open ports.
open_ports = []

# Loop through each line of the command output, skipping the header line.
for line in output.splitlines()[1:]:
    # Split the line into parts using whitespace as the delimiter.
    parts = line.split()

    # Ensure the line has more than 4 parts before proceeding to avoid index errors.
    if len(parts) > 4:
        # The first part is the protocol (e.g., tcp, udp).
        proto = parts[0]

        # The fifth part is the local address and port.
        local_address = parts[4]

        # Check if the local address contains a colon, indicating an IPv4 address with a port.
        if ':' in local_address:
            # Extract the port number from the local address.
            port = local_address.split(':')[-1]

            # Append the protocol and port number as a tuple to the open_ports list.
            open_ports.append((proto, port))

# Initialize an empty list to store the final report data.
report = []

# Loop through each protocol and port pair in the open_ports list.
for proto, port in open_ports:
    try:
        # Attempt to get the service name associated with the port number.
        service_name = socket.getservbyport(int(port))
    except:
        # If the port number is not recognized, set the service name to "Unknown".
        service_name = "Unknown"

    # Initialize the function description to "N/A" (not available).
    function = "N/A"

    # Open the /etc/services file in read mode to look up the service description.
    with open('/etc/services', 'r') as f:
        for line in f:
            # Check if the line starts with the service name.
            if line.startswith(service_name):
                # Extract the function description from the comment, if available.
                function = line.split('#')[-1].strip() if '#' in line else "N/A"
                break

    # Append the collected data to the report list as a dictionary.
    report.append({
        "Protocol": proto,          # Network protocol (TCP or UDP).
        "Port Number": port,        # Port number.
        "Service Name": service_name,  # Name of the service associated with the port.
        "Function": function        # Function or description of the service.
    })

# Create a pandas DataFrame from the report list for structured data manipulation and analysis.
df = pd.DataFrame(report)

# Print the DataFrame to the console to display the report.
print(df)
