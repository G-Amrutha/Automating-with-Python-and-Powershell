# Top CPU Processes Monitor

This PowerShell script retrieves and displays the top five processes consuming the most CPU resources on your system. It's useful for system administrators and users who need to monitor performance and identify resource-intensive applications.

## Features

- Lists all running processes.
- Sorts processes by CPU usage in descending order.
- Displays the top five processes with the highest CPU usage.
- Outputs results in a neatly formatted table for easy readability.

## Requirements

- Windows operating system with PowerShell installed.
- Appropriate permissions to run PowerShell scripts.

## Usage

1. **Open PowerShell:**
   - Press `Win + R`, type `powershell`, and press `Enter`.

2. **Run the Script:**
   - Copy the following script into your PowerShell terminal and press `Enter`:

   ```powershell
   # Retrieve a list of all running processes and sort them in descending order based on CPU usage
   $topProcesses = Get-Process | Sort-Object -Property CPU -Descending

   # Select the top five processes from the sorted list, displaying only the Id, ProcessName, and CPU properties
   $topFiveProcesses = $topProcesses | Select-Object -First 5 -Property Id, ProcessName, CPU

   # Format the selected processes into a table with columns automatically sized for readability
   $topFiveProcesses | Format-Table -AutoSize
