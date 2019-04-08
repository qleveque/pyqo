import sys
import pyttsx3

command = ' '.join(sys.argv[1:])

speech = command
engine = pyttsx3.init()
engine.say(speech)
engine.runAndWait()