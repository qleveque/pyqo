import sys
import os
import re
import shutil
from _reader import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dir = '../scripts'
particulars = {'c' :
                {'windows' : 'call  %~dp0/_c.bat\n',
                'linux' : ''}
              }

if sys.platform in ['linux', 'linux2']:
    ext = ''
    
    def script_content(command) :
        r = """ """
        if command in particulars:
            r+=particulars[command]['linux']
        return r
        
    def a_script_content(command):
        pass

else:
    ext = '.bat'
    
    def script_content(command) :
        r = """@echo off
python %~dp0/../python/{}.py %*
""".format(command)
        if command in particulars:
            r+=particulars[command]['windows']
        return r
    
    def a_script_content(command):
        return "@{} %*".format(command)

def write_scripts():
    if os.path.isdir('../scripts'):
        shutil.rmtree('../scripts')
    os.mkdir('../scripts')

    files = os.listdir()
    pattern = re.compile("^[^_].*.py$")
    files = [file for file in files if pattern.match(file)]
    commands = [file[:-3] for file in files]
    
    for command in commands:
        file = os.path.join(dir, command+ext)
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(script_content(command))
            
    a_data = read_json('../data/a.json')
    for key, value in a_data.items():
        file = os.path.join(dir, key+ext)
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(a_script_content(value))
            
if __name__ == '__main__':
    write_scripts()