import speech_recognition as sr
from googletrans import Translator
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 125)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


r = sr.Recognizer()
speech = sr.AudioFile('OSR_us_000_0061_8k.wav')
print('audio uploaded....')
with speech as source:
    audio = r.record(source)

text = r.recognize_google(audio, show_all=True)

text1 = text['alternative'][0]['transcript']
engine.say(text1)
engine.runAndWait()
print(text1)
# print(len(text1))


translator = Translator()
translations = translator.translate([text1], dest='gu')
for translation in translations:
    print(translation.text)

