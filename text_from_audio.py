import urllib2
import speech_recognition as sr
import subprocess
import os

url = 'https://cdn.fbsbx.com/v/t59.3654-21/15720510_10211855778255994_5430581267814940672_n.mp4/audioclip-1484407992000-3392.mp4?oh=a78286aa96c9dea29e5d07854194801c&oe=587C3833'
mp4file = urllib2.urlopen(url)

with open("test.mp4", "wb") as handle:
    handle.write(mp4file.read())

cmdline = ['avconv',
           '-i',
           'test.mp4',
           '-vn',
           '-f',
           'wav',
           'test.wav']
subprocess.call(cmdline)

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

command = r.recognize_google(audio)
print(command)

os.remove("test.mp4")
os.remove("test.wav")


####################################################################

import speech_recognition as sr

r = sr.Recognizer()

audio = 'trial.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)

except Exception as e:
    print (e)