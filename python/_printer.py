WIDTH = 19
PER_LINE = 4

def print_list(datas):
    r = ""
    for idx,data in enumerate(sorted(datas)):
        r+="{d:<{width}}".format(d=data, width=WIDTH)
        if (idx+1)%PER_LINE == 0:
            r+="\n"
    print(r)
