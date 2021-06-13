import speech_recognition as sr
import pyttsx3

#asd

def speak(text):
    engine = pyttsx3.init("espeak")
    rate = engine.getProperty("rate")
    engine.setProperty("rate",160)
    engine.setProperty("voice","en-uk")
    engine.say(text)
    engine.runAndWait()


def get_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        speech = ""
        try:
            speech = r.recognize_google(audio)
            print(speech)
        except Execption as e:
            print("Exception: " + str(e))
    return speech

#################################3

#get_speech()
#speak("hello")

wake = "hello Ben"
while True:
    text = get_speech()
    if text.count(wake) > 0:
        speak("How do you do sir")
#        text = get_audio

