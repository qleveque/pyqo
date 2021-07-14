import platform
import os
from subprocess import call, Popen, DEVNULL, PIPE, STDOUT


def is_wsl():
    return (platform.system()=='Linux' and
           'microsoft' in platform.uname().release.lower())


def wsl_path(command):
    proc = Popen(command,
                 shell=True,
                 stdout=PIPE,
                 stderr=PIPE)
    stdout, stderr = proc.communicate()
    if stderr:
        exit(stderr.decode('utf-8'))
    return stdout.decode('utf-8').strip()


def wsl_linux_path(path):
    return wsl_path('wslpath -a -u "{}"'.format(path))


def wsl_windows_path(path):
    return wsl_path('wslpath -a -m "{}"'.format(path))


def os_open(to_open):
    if platform.system()=='Windows':
        cmd = 'start "" "{}"'.format(to_open)

    elif is_wsl(): 
        cmd = 'cmd.exe /C start "" "{}"'.format(to_open)

    elif platform.system()=='Linux':
        cmd = 'xdg-open "{}"'.format(to_open)

    else:
        exit('Unknown OS. Exiting.')

    call(cmd, shell=True)

