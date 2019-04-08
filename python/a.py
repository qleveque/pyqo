import sys
import os
import subprocess
from _reader import *

cwd = os.getcwd()
os.chdir(sys.path[0])

filename = '../data/a.json'

for i in range(len(sys.argv)):
    #if os.path.isabs(sys.argv[i]):
    #    sys.argv[i] = '"'+sys.argv[i]+'"'
    if ' ' in sys.argv[i]:
        sys.argv[i] = '"'+sys.argv[i]+'"'
        
if har(filename, sys.argv[1:]):
    exit()
    
from _write_scripts import *
write_scripts()