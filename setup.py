import sys
import subprocess
import os
sys.path.append('python')
from _write_scripts import *

current_path = os.path.dirname(os.path.abspath(__file__))
SCRIPTS  = os.path.join(current_path, 'scripts')

def addLines(filename, content, add):
	with open(filename, "r+") as file:
		for line in file:
			if content in line:
				return
		file.write(add)

if sys.platform in ['linux', 'linux2']:
	#profile
	content_flag = "#PYQ_START"

	add_profile = """
#PYQ_START
PATH="{}:$PATH"
#PYQ_END
""".format(SCRIPTS)
	addLines("{}/.profile".format(os.environ['HOME']), content_flag, add_profile)

	add_bashrc = """
#PYQ_START
alias c='source c'
#PYQ_END
"""
	addLines("{}/.bashrc".format(os.environ['HOME']), content_flag, add_bashrc)

else:
    script_to_add = """
#Include %A_ScriptDir%\\env.ahk
Env_UserAdd("PATH","{}")
Env_SystemRemoveDuplicates("PATH")
""".format(SCRIPTS)
    
    AHK_SCRIPT = os.path.join(current_path,'config','windows','add_path.ahk')
    with open(AHK_SCRIPT, 'w', encoding = 'utf-8') as f:
        f.write(script_to_add)
    
    subprocess.call('open {}'.format(AHK_SCRIPT),shell=True)

write_scripts()
