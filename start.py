import sys
import subprocess
import os

current_path = os.path.dirname(os.path.abspath(__file__))

if sys.platform in ['linux', 'linux2']:
    pass
else:
    pyq = os.path.join(current_path, 'batches')
    subprocess.call('setx PATH "%PATH%;{}"'.format(pyq), shell=True)