import sys
import os
from _reader import *

os.chdir(sys.path[0])

filename = '../data/v.json'
config = read_json('../config.json')
if 'shared_dir' in config and config['shared_dir']!='':
        filename = os.path.join(config['shared_dir'],'v.json')

if har(filename, sys.argv[1:]):
    exit()
        
data = read_json(filename)
    
if len(sys.argv)>=2 and sys.argv[1] in data:
    print(data[sys.argv[1]])