import sys
import os
from _reader import *

filename = os.path.join(sys.path[0], '../data/c.json')
end_file = os.path.join(sys.path[0],'../scripts/_c.bat')

if har(filename, sys.argv[1:], file=True, add_default = os.getcwd()):
    with open(end_file,'w', encoding = 'utf-8') as f:
        f.write('')
    exit()

data = read_json(filename)
    
to_write = ''
if len(sys.argv)>=2 and sys.argv[1] in data:
    to_write = 'cd {}\n'.format(data[sys.argv[1]])
    
with open(end_file,'w', encoding = 'utf-8') as f:
    f.write(to_write)