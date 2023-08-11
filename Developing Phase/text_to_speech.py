import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech("My name is Akshay")