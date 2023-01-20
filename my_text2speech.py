import pyttsx3

def t2s(text):
    text_speech = pyttsx3.init()
    try:
        text_speech.say(text)
        text_speech.runAndWait()

    except Exception as e:

        print("Error : " + str(e))
