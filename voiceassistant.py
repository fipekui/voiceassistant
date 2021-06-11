import speech_recognition as sr
 
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("Please say something")
    audio = r.listen(source)
    speech = r.recognize_google(audio)
    print(speech)
