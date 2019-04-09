import sys
import subprocess
import os
sys.path.append('python')
from _write_scripts import *

current_path = os.path.dirname(os.path.abspath(__file__))

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
""".format(os.path.join(current_path,'scripts'))
	addLines("{}/.profile".format(os.environ['HOME']), content_flag, add_profile)

	add_bashrc = """
#PYQ_START
alias c='source c'
#PYQ_END
"""
	addLines("{}/.bashrc".format(os.environ['HOME']), content_flag, add_bashrc)

else:
	#TODO
	#pyq = os.path.join(current_path, 'scripts')
	#subprocess.call('setx /M PATH "%PATH%;{}"'.format(pyq), shell=True)
	print("You need to manually add the following folder to your PATH environment variable:")
	print(os.path.join(current_path,'scripts'))

write_scripts()
