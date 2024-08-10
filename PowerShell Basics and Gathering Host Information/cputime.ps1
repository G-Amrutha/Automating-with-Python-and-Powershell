$topProcesses = Get-Process | Sort-Object -Property CPU -Descending
$topFiveProcesses = $topProcesses | Select-Object -First 5 -Property Id, ProcessName, CPU
$topFiveProcesses | Format-Table -AutoSize
