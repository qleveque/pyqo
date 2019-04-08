import sys
import subprocess
import os
sys.path.append('python')
from _write_scripts import *

current_path = os.path.dirname(os.path.abspath(__file__))
write_scripts()

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
alias c='source c'
#PYQ_END
""".format(os.path.join(current_path,'scripts'))
	addLines("{}/.profile".format(os.environ['HOME']), content_flag, add_profile)

else:
	#TODO
	#pyq = os.path.join(current_path, 'batches')
	#subprocess.call('setx /M PATH "%PATH%;{}"'.format(pyq), shell=True)
	#config = os.path.join(current_path, 'windows_config')
	#subprocess.call('setx /M PATH "%PATH%;{}"'.format(config), shell=True)
	pass
