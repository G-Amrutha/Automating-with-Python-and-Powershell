#!/usr/bin/env python3
# Script Name: top_five.py
# Purpose: Generate a report of the top 5 processes by CPU usage and display it.

import subprocess
# Importing the subprocess module to run Linux system commands.

import pandas as pd
# Importing the pandas module for data manipulation and analysis, useful for handling tabular data.

# Running the 'ps aux --sort=-%cpu' command to list all running processes,
# sorted by CPU usage in descending order, and capturing the output.
result = subprocess.run(['ps', 'aux', '--sort=-%cpu'], stdout=subprocess.PIPE)

# Decoding the captured output from bytes to a string, then splitting it into lines based on newline characters.
process_data = result.stdout.decode('utf-8').split('\n')

# Splitting the first line (header) into individual column names.
headers = process_data[0].split()

# Getting all lines except the first one, which contain the process data.
process_lines = process_data[1:]

# Initializing an empty list to store information about processes.
process_list = []

# Looping through each line of the process data.
for line in process_lines:

    if line:
        # Checking if the line is not empty.

        # Splitting the line into parts, with the number of parts matching the number of headers.
        # The 'None' argument allows splitting by any whitespace, and 'len(headers) - 1' ensures
        # the last column (COMMAND) captures all remaining text.
        process_info = line.split(None, len(headers) - 1)

        # Appending the split process information to the process_list.
        process_list.append(process_info)

# Creating a pandas DataFrame from the process_list, using the headers for column names.
df = pd.DataFrame(process_list, columns=headers)

# Converting the '%CPU' column to float type for numerical operations.
df['%CPU'] = df['%CPU'].astype(float)

# Selecting the top 5 processes with the highest CPU usage.
top_processes = df.nlargest(5, '%CPU')

# Printing a header for the output.
print("TOP FIVE PROCESSES BY CPU USAGE:")

# Printing the selected columns of the top 5 processes DataFrame.
print(top_processes[['USER', 'PID', '%CPU', '%MEM', 'COMMAND']])
