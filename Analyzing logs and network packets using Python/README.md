# Python Script Collection

This repository contains three Python scripts designed for different purposes, including log analysis, network traffic sniffing, and visualization of log data frequency.

## Scripts Overview

### 1. applog.py

**Description**: 
This script reads and processes a CSV file named `appevent.csv` to analyze application event logs.

**Features**:
- Reads the event log CSV file using Pandas.
- Displays the last entry of the dataset.
- Prints the names of all columns in the CSV file.
- Shows a frequency count of unique values in the "Source" column.

**Usage**:
1. Ensure the `appevent.csv` file is in the same directory as the script.
2. Run the script using Python:

   ```bash
   python applog.py
   ```

### 2. sniff.py

**Description**: 
This script uses the `scapy` library to sniff network packets on a specified network interface, displaying IP packets' source and destination details.

**Features**:
- Captures network traffic on the "Wi-Fi" interface.
- Sniffs 10 IP packets.
- Prints the source and destination IP addresses along with the protocol for each packet.

**Usage**:
1. Ensure you have `scapy` installed.
2. Run the script using Python:

   ```bash
   python sniff.py
   ```

**Note**: Administrative privileges might be required to run this script depending on your network settings.

### 3. logfreq.py

**Description**: 
This script processes a CSV file named `appevent.csv` to analyze and visualize the frequency of log entries over time.

**Features**:
- Reads and prints the names of columns in the CSV file.
- Extracts and converts timestamp columns to datetime format.
- Generates and displays a frequency plot of log entries grouped by month.

**Usage**:
1. Ensure the `appevent.csv` file is in the same directory as the script.
2. Run the script using Python:

   ```bash
   python logfreq.py
   ```

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **Required Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `matplotlib`: For data visualization.
  - `scapy`: For network packet sniffing (required by `sniff.py`).

Install the required Python libraries using pip:

```bash
pip install pandas matplotlib scapy
```

## Files

- **`appevent.csv`**: A CSV file required for `applog.py` and `logfreq.py`, containing application event logs.
