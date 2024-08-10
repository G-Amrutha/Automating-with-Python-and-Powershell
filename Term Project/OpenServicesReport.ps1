# Script Name: OpenServicesReport.ps1
# Purpose: Generate a report of active listening TCP and UDP connections along with their associated services and export it to a CSV file.

# Get active listening TCP connections by filtering only those in the "Listen" state
$tcpListenConnections = Get-NetTCPConnection | Where-Object { $_.State -eq "Listen" }

# Get active UDP endpoints (UDP is connectionless so endpoints are considered "open")
$udpListenEndpoints = Get-NetUDPEndpoint

# Retrieve information about all system services
$systemServices = Get-WmiObject -Class Win32_Service

# Initialize an empty array to store the network report data
$networkReport = @()

# Loop through each listening TCP connection to associate it with the corresponding service
foreach ($tcpConnection in $tcpListenConnections) {
    # Find the service associated with the TCP connection's owning process ID
    $associatedService = $systemServices | Where-Object { $_.ProcessId -eq $tcpConnection.OwningProcess }
    
    # If an associated service is found, create a custom object with connection details and add it to the report
    if ($associatedService) {
        $networkReport += [PSCustomObject]@{
            Protocol    = "TCP"                               # Protocol type
            PortNumber  = $tcpConnection.LocalPort            # TCP port number
            ServiceName = $associatedService.Name             # Service name
            Function    = $associatedService.DisplayName      # Service display name (function)
        }
    }
}

# Loop through each UDP endpoint to associate it with the corresponding service
foreach ($udpEndpoint in $udpListenEndpoints) {
    # Find the service associated with the UDP endpoint's owning process ID
    $associatedService = $systemServices | Where-Object { $_.ProcessId -eq $udpEndpoint.OwningProcess }
    
    # If an associated service is found, create a custom object with endpoint details and add it to the report
    if ($associatedService) {
        $networkReport += [PSCustomObject]@{
            Protocol    = "UDP"                               # Protocol type
            PortNumber  = $udpEndpoint.LocalPort              # UDP port number
            ServiceName = $associatedService.Name             # Service name
            Function    = $associatedService.DisplayName      # Service display name (function)
        }
    }
}

# Export the network report data to a CSV file named "OpenNetworkServicesReport.csv" without including type information
$networkReport | Export-Csv -Path "OpenNetworkServicesReport.csv" -NoTypeInformation

# Display the formatted report in the console using a table layout with automatic column sizing
$networkReport | Format-Table -AutoSize
