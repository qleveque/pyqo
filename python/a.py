import sys
import os
import subprocess
from _reader import *

filename = os.path.join(sys.path[0],'../data/a.json')

for i in range(len(sys.argv)):
    if ' ' in sys.argv[i]:
        sys.argv[i] = '"'+sys.argv[i]+'"'
    elif sys.argv[i]=='':
        sys.argv[i] = '""'

if har(filename, sys.argv[1:]):
    exit()

from _write_scripts import *
write_scripts()
