import random
import sys

max = 100
if len(sys.argv)>=2:
    max = int(sys.argv[1])

rand = random.randint(0,max)
print(rand)