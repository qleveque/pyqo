import sys
import os
import subprocess
from _reader import *

filename = os.path.join(sys.path[0],'../data/c.json')

if har(filename, sys.argv[1:], file=True):
    exit()

data = read_json(filename)

if len(sys.argv)>=2:
    if sys.argv[1] in data:
        dir_ = data[sys.argv[1]]
else:
    dir_ = os.getcwd()

if sys.platform in ['linux', 'linux2']:
    cmd = 'xdg-open ' + dir_
else:
    cmd = 'open "' + dir_+'"'
    print(cmd)

subprocess.call(cmd, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
