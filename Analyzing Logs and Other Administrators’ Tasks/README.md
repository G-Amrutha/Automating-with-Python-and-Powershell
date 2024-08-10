# Get-DiskUsage

`Get-DiskUsage` is a PowerShell script that retrieves and displays disk usage information for the current directory and its subdirectories. It provides an option to include the size of subdirectories in the total size calculation for each directory.

## Features

- Calculates disk usage for the current directory.
- Optionally includes the size of all subdirectories in the total size calculation.
- Provides output in a clear and readable format with directory names and sizes.

## Requirements

- Windows operating system with PowerShell installed.
- Appropriate permissions to run PowerShell scripts in the target directory.

## Usage

1. **Open PowerShell:**
   - Press `Win + R`, type `powershell`, and press `Enter`.

2. **Run the Script:**
   - Copy the following script into a PowerShell file (e.g., `Get-DiskUsage.ps1`) or directly into the PowerShell terminal.

   ```powershell
   ##############################################################################
   ##
   ## Get-DiskUsage
   ##
   ## From Windows PowerShell Cookbook (O'Reilly)
   ## by Lee Holmes (http://www.leeholmes.com/guide)
   ##
   ##############################################################################

   <#

   .SYNOPSIS

   Retrieve information about disk usage in the current directory and all
   subdirectories. If you specify the -IncludeSubdirectories flag, this
   script accounts for the size of subdirectories in the size of a directory.

   .EXAMPLE

   PS > Get-DiskUsage
   Gets the disk usage for the current directory.

   .EXAMPLE

   PS > Get-DiskUsage -IncludeSubdirectories
   Gets the disk usage for the current directory and those below it,
   adding the size of child directories to the directory that contains them.

   #>

   param(
       ## Switch to include subdirectories in the size of each directory
       [switch] $IncludeSubdirectories
   )

   Set-StrictMode -Version 3

   ## If they specify the -IncludeSubdirectories flag, then we want to account
   ## for all subdirectories in the size of each directory
   if($IncludeSubdirectories)
   {
       Get-ChildItem -Directory |
           Select-Object Name,
               @{ Name="Size";
               Expression={ ($_ | Get-ChildItem -Recurse |
                   Measure-Object -Sum Length).Sum + 0 } }
   }
   ## Otherwise, we just find all directories below the current directory,
   ## and determine their size
   else
   {
       Get-ChildItem -Recurse -Directory |
           Select-Object FullName,
               @{ Name="Size";
               Expression={ ($_ | Get-ChildItem |
                   Measure-Object -Sum Length).Sum + 0 } }
   }
