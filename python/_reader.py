import json
import os

def read_json(path):
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as f:
            data = json.loads(f.read())
    else:
        data = {}
    return data

def har(filename, args, **kwargs):
    if len(args)<1:
        return False
    HELP = ['-h','--help']
    ADD = ['-a','--add']
    REMOVE = ['-r','--remove']
    if args[0] not in HELP+ADD+REMOVE:
        return False
      
    data = read_json(filename)
      
    if args[0] in HELP:
        print(data)
        return True
        
    if args[0] in ADD:
        if len(args)>=3:
            to_add = ' '.join(args[2:])
            if 'file' in kwargs and kwargs['file']:
                if os.path.exists(to_add) and not os.path.isabs(to_add):
                    to_add = os.path.join(os.getcwd(),to_add)
                to_add = to_add.replace('\\','/')
        elif len(args)>=2 and 'add_default' in kwargs:
            to_add = kwargs['add_default']
        else:
            return True
        data[args[1]] = to_add
        
    elif args[0] in REMOVE and len(args)>=2:
        if args[1] in data:
            data.pop(args[1])
            
    with open(filename, 'w', encoding = 'utf-8') as f:
        json.dump(data, f)
    
    return True
        
    
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as f:
            data = json.loads(f.read())
    else:
        data = {}
    return data