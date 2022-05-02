import speech_recognition as sr
r = sr.Recognizer()

i = 0
with sr.WavFile("Testament.wav") as source:       
      while i < 800:
        audio = r.record(source, duration = 240)                                  # reading the entire audio file from a wav file
        texte = r.recognize_google(audio, language= "fr-FR")                      # recording the entire audio file in French
        print(texte)
        file = open('transcription.txt', 'a')                                     # appending the transcripted audio file in a txt file
        file.write(texte) 
        file.close() 
        i+=240