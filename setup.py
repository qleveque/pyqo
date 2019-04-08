import sys
import subprocess
import os
sys.path.append('python')
from _write_scripts import *

current_path = os.path.dirname(os.path.abspath(__file__))
write_scripts()

if sys.platform in ['linux', 'linux2']:
    pass
else:
    #TODO
    #pyq = os.path.join(current_path, 'batches')
    #subprocess.call('setx /M PATH "%PATH%;{}"'.format(pyq), shell=True)
    #config = os.path.join(current_path, 'windows_config')
    #subprocess.call('setx /M PATH "%PATH%;{}"'.format(config), shell=True)
    pass
    