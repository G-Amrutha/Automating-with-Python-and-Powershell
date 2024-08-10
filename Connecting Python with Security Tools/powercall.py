import os
import subprocess
import sys
import pandas as pd

print('Running PowerShell scripts\n')

subprocess.Popen(["powershell.exe", ".\listservice.ps1"], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True,universal_newlines = True)

#read the information in the dataframe
df=pd.read_csv('service.csv',encoding="ISO-8859-1",skiprows=1)
print(df['Name'])
