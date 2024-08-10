# System Processes and Services Report Scripts

## Overview

This section contains scripts designed to generate reports on system processes and open network services. These scripts help identify resource-intensive processes and active network connections, providing insights into system performance and network activity.

### Scripts

1. **top_five.py**: Generates a report of the top 5 processes by CPU usage on a Linux system and displays it.
2. **services_report.py**: Generates a report of open network ports, their associated services, and functions on a Linux system.
3. **Top5ProcessesReport.ps1**: Generates a report of the top 5 processes by CPU usage on a Windows system and exports it to a CSV file.
4. **OpenServicesReport.ps1**: Generates a report of active listening TCP and UDP connections on a Windows system along with their associated services and exports it to a CSV file.

## Requirements

### Linux

- Python 3.x
- Pandas library

To install Pandas, run:
```bash
pip install pandas
```

### Windows

- PowerShell

## Usage

### Top Five Processes by CPU Usage (Linux)

**Script**: `top_five.py`

This script retrieves and displays the top 5 processes consuming the most CPU resources.

#### How to run:

```bash
python3 top_five.py
```

### Open Network Services Report (Linux)

**Script**: `services_report.py`

This script lists open network ports along with the service names and functions associated with them.

#### How to run:

```bash
python3 services_report.py
```

### Top Five Processes by CPU Usage (Windows)

**Script**: `Top5ProcessesReport.ps1`

This PowerShell script retrieves the top 5 processes by CPU usage and exports the data to a CSV file.

#### How to run:

```powershell
powershell -ExecutionPolicy Bypass -File .\Top5ProcessesReport.ps1
```

### Open Network Services Report (Windows)

**Script**: `OpenServicesReport.ps1`

This PowerShell script generates a report of active listening TCP and UDP connections with their associated services and exports it to a CSV file.

#### How to run:

```powershell
powershell -ExecutionPolicy Bypass -File .\OpenServicesReport.ps1
```

### Notes

- Ensure you have the necessary permissions to execute these scripts on your system.
- Modify file paths or network settings as needed for your specific environment.
- Use these scripts for monitoring and analysis in controlled environments.
