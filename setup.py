import sys
import subprocess
import os
sys.path.append('python')
from _write_scripts import *

current_path = os.path.dirname(os.path.abspath(__file__))
SCRIPTS  = os.path.join(current_path, 'scripts')

if sys.platform in ['linux', 'linux2']:
	START_FLAG = "#PYQ_START"
	END_FLAG = "#PYQ_END"

	BASHRC = os.path.join(format(os.environ['HOME']),".bashrc")
	PROFILE = os.path.join(format(os.environ['HOME']),".profile")

	TO_ADD_PROFILE = """{start}
PATH="{scripts}:$PATH"
{end}
""".format(start = START_FLAG, scripts = SCRIPTS, end = END_FLAG)
	TO_ADD_BASHRC = """{start}
alias c='source c'
{end}
""".format(start = START_FLAG, end = END_FLAG)

	def add_lines(filename, flag, add):
		with open(filename, "r+") as file:
			for line in file:
				if flag in line:
					return
			file.write(add)

	def remove_lines(filename, start, end):
		with open(filename, "r+") as f:
			d = f.readlines()
			consider_line = True
			f.seek(0)
			for l in d:
				if l.strip() == start:
					consider_line = False
				if consider_line:
					f.write(l)
				if l.strip() == end:
					consider_line = True
			f.truncate()

	def setup():
		remove_lines(PROFILE, START_FLAG, END_FLAG)
		remove_lines(BASHRC, START_FLAG, END_FLAG)
		add_lines(PROFILE, START_FLAG, TO_ADD_PROFILE)
		add_lines(BASHRC, START_FLAG, TO_ADD_BASHRC)

	def uninstall():
		remove_lines(PROFILE, START_FLAG, END_FLAG)
		remove_lines(BASHRC, START_FLAG, END_FLAG)

else:
	SCRIPT_TO_ADD = """
#Include %A_ScriptDir%\\env.ahk
Env_UserAdd("PATH","{}")
Env_SystemRemoveDuplicates("PATH")
""".format(SCRIPTS)

	SCRIPT_TO_SUB = """
#Include %A_ScriptDir%\\env.ahk
Env_UserSub("PATH","{}")
Env_SystemRemoveDuplicates("PATH")
""".format(SCRIPTS)

	def setup():
		AHK_SCRIPT = os.path.join(current_path,'config','windows','add_path.ahk')
		with open(AHK_SCRIPT, 'w', encoding = 'utf-8') as f:
			f.write(SCRIPT_TO_ADD)
		subprocess.call('open {}'.format(AHK_SCRIPT),shell=True)

	def uninstall():
		AHK_SCRIPT = os.path.join(current_path,'config','windows','sub_path.ahk')
		with open(AHK_SCRIPT, 'w', encoding = 'utf-8') as f:
			f.write(SCRIPT_TO_SUB)
		subprocess.call('open {}'.format(AHK_SCRIPT),shell=True)

if __name__ == "__main__":
	args = sys.argv
	if len(args)>=2 and args[1]=='uninstall':
		uninstall()
		print('pyq successfully uninstalled.')
	else:
		setup()
		print('pyq successfully set up.')
