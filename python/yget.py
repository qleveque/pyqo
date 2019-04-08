import pytube
import sys
import os

cwd = os.getcwd()
val = sys.argv[1]

print("Downloading {}".format(val))

try:
    yt = pytube.YouTube(val)
    stream = yt.streams.first()
    stream.download(cwd)
except Exception as e:
    print(e)
    input("Press Enter to continue...")