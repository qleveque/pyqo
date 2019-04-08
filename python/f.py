import sys
import os
import subprocess
from _reader import *

os.chdir(sys.path[0])

filename = '../data/f.json'

if har(filename, sys.argv[1:], file=True):
    exit()

data = read_json(filename)

if len(sys.argv)>=2 and sys.argv[1] in data:
    file = data[sys.argv[1]]
    
    if sys.platform in ['linux', 'linux2']:
        cmd = 'xdg-open ' + file
    else:
        cmd = 'open "' + file+'"'
    
    subprocess.call(cmd, shell=True)