import subprocess
import os

path = r'D:\SAMAN\test22222'
os.chdir(path)
a =  subprocess.check_output('git log', shell=True, text=True)

print(str(a))



