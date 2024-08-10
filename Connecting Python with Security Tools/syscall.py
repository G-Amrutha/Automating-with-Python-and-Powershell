import os
import subprocess
import sys

print('Using subprocess : \n')
res=subprocess.check_output('dir ',shell=True)

print(res)

print('\nUsing os : \n')
output = os.popen('dir').readlines()
print(output)

print('Running a command\n')
subprocess.call('echo hello world > test.txt',shell=True)
