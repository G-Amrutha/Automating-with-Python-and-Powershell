# Python and PowerShell Script Collection

This repository contains various Python and PowerShell scripts for tasks such as log analysis, network scanning, service management, and more. Each script is designed to perform specific operations, making it easy to manage and analyze system data.

## Scripts Overview

### 1. applog.py

**Description**: 
This script processes an event log CSV file (`appevent.csv`) to analyze application events.

**Features**:
- Reads and displays the last entry of the dataset.
- Prints column names.
- Shows the frequency count of unique values in the "Source" column.

**Usage**:
```bash
python applog.py
```

### 2. sniff.py

**Description**: 
Captures network packets using `scapy` to display source and destination IP details.

**Features**:
- Sniffs 10 IP packets on the "Wi-Fi" interface.
- Displays source and destination IP addresses and protocol.

**Usage**:
```bash
python sniff.py
```

**Note**: Administrative privileges might be required.

### 3. logfreq.py

**Description**: 
Analyzes log entry frequency over time from `appevent.csv`.

**Features**:
- Extracts and converts timestamps.
- Generates a frequency plot of log entries by month.

**Usage**:
```bash
python logfreq.py
```

### 4. listservice.ps1

**Description**: 
PowerShell script that lists all running services and exports them to a CSV file.

**Features**:
- Retrieves running services using PowerShell.
- Exports service information to `service.csv`.

**Usage**:
Run the script in PowerShell:
```powershell
powershell.exe -File .\listservice.ps1
```

### 5. logfreqbyname.py

**Description**: 
Processes a specified log CSV file to analyze log frequency by timestamps.

**Features**:
- Reads a specified CSV file.
- Converts and extracts timestamps.
- Generates a frequency plot of log entries by month.

**Usage**:
```bash
python logfreqbyname.py <filename>
```

### 6. portscan.py

**Description**: 
Performs a port scan on localhost using the `nmap` library.

**Features**:
- Scans ports 22 to 443 on `127.0.0.1`.
- Displays command line, output format, host state, and open ports.

**Usage**:
```bash
python portscan.py
```

**Note**: Requires `nmap` to be installed on your system.

### 7. powercall.py

**Description**: 
Executes a PowerShell script and reads service information from a CSV file.

**Features**:
- Runs `listservice.ps1`.
- Reads and displays service names from `service.csv`.

**Usage**:
```bash
python powercall.py
```

### 8. syscall.py

**Description**: 
Executes shell commands using `os` and `subprocess` modules.

**Features**:
- Lists directory contents.
- Executes shell commands and outputs results.

**Usage**:
```bash
python syscall.py
```

### 9. systest.py

**Description**: 
Demonstrates usage of command-line arguments in Python.

**Features**:
- Prints script name, number of arguments, and argument values.

**Usage**:
```bash
python systest.py arg1 arg2 arg3
```

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed.
- **Required Libraries**:
  - `pandas`, `matplotlib`, `scapy` (for network sniffing), `nmap` (for port scanning).
- **PowerShell**: For running PowerShell scripts.

Install the required Python libraries using pip:

```bash
pip install pandas matplotlib scapy python-nmap
```

### Notes:

- Ensure that the file paths and names match your actual setup.
- Make sure to run `listservice.ps1` with appropriate permissions.
- Adjust the network interface in `sniff.py` and the host IP in `portscan.py` as necessary.
