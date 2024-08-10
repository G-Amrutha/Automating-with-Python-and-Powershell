# Script Name: Top5ProcessesReport.ps1
# Purpose: Generate a report of the top 5 processes by CPU usage and export it to a CSV file.

# Retrieve all running processes and sort them by CPU time used in descending order
$topProcesses = Get-Process | Sort-Object -Property CPU -Descending

# Select the top five processes based on CPU usage
$topFiveProcesses = $topProcesses | Select-Object -First 5 -Property Id, ProcessName, CPU, Description

# Output the selected processes in a formatted table
$topFiveProcesses | Format-Table -AutoSize

# Export the selected processes to a CSV file
$topFiveProcesses | Export-Csv -Path "TopFiveCPUProcesses.csv" -NoTypeInformation
