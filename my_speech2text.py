import speech_recognition as sr

def s2t():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")

        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
        