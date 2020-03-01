import platform
import os
from subprocess import call, Popen, DEVNULL, PIPE, STDOUT

def os_open(to_open):
    if platform.system()=='Windows':
        cmd = 'start "" "{}"'.format(to_open)

    elif 'microsoft' in platform.uname()[3].lower():
        # WSL
        if os.path.exists(to_open):
            proc = Popen('wslpath -a -m "{}"'.format(to_open),
                        shell=True,
                        stdout=PIPE,
                        stderr=PIPE)
            stdout, stderr = proc.communicate()
            if stderr:
                exit(stderr.decode('utf-8'))
            to_open = stdout.decode('utf-8').strip()
        cmd = 'cmd.exe /C start "" "{}"'.format(to_open)

    elif platform.system()=='Linux':
        cmd = 'xdg-open "{}"'.format(to_open)

    else:
        exit('Unknown OS. Exiting.')

    call(cmd, shell=True)


