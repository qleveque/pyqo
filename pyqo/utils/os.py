import platform
from subprocess import call, Popen, PIPE


def is_wsl():
    return (platform.system()=='Linux' and
           'microsoft' in platform.uname().release.lower())

def popen(command: str):
    proc = Popen(command,
                 shell=True,
                 stdout=PIPE,
                 stderr=PIPE)
    stdout, stderr = proc.communicate()
    if stderr:
        exit(stderr.decode('utf-8'))
    return stdout.decode('utf-8').strip()

def wsl_linux_path(path: str):
    return popen(f'wslpath -a -u "{path}"')

def wsl_windows_path(path: str):
    return popen(f'wslpath -a -m "{path}"')

def os_open(to_open: str):
    if platform.system()=='Windows':
        cmd = f'start "" "{to_open}"'

    elif is_wsl():
        cmd = f'cmd.exe /C start "" "{to_open}"'

    elif platform.system()=='Linux':
        cmd = f'xdg-open "{to_open}"'

    else:
        exit('Unknown OS. Exiting.')

    call(cmd, shell=True)
