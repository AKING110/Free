import os,platform
chk = platform.architecture()[0]
if '64bit' in chk:
    if path.isfile("dump"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/AKING110/projects/main/dump -o dump')
    if path.isfile("XD"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/AKING110/projects/main/XD -o XD')
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')
