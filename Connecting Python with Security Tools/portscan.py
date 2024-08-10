import nmap

nmScan = nmap.PortScanner()

nmScan.scan('127.0.0.1', '22-443','-sV')

print('Command Line: ',nmScan.command_line())
print('Output Format: ',nmScan.csv())

print('Scan Info: ',nmScan.scaninfo())

print('All hosts: ',nmScan.all_hosts())

print('Host Name: ',nmScan['127.0.0.1'].hostname())

print('Host State: ',nmScan['127.0.0.1'].state())

print('Protocol: ',nmScan['127.0.0.1'].all_protocols())


print('Open Ports: ',nmScan['127.0.0.1']['tcp'].keys())

