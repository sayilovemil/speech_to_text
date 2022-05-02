import speech_recognition as sr

# obtain path to "file.extention" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "Testament.wav")

# use the audio file as the audio source
r = sr.Recognizer()

i = 0
with sr.AudioFile(AUDIO_FILE) as source:
    while i < 803:
        audio = r.record(source, duration = 240)  # read the entire audio file
        texte = r.recognize_google(audio, language= "fr-FR")
        print(texte)
        i+=240
