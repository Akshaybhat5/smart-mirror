import speech_recognition as sr
from text_to_speech import text_to_speech

def speech_to_text():
    
    
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            
            text_to_speech("How can I help you?")
            audio = recognizer.listen(source, timeout=None)

        try:
            text = recognizer.recognize_google(audio)
            print("you said: ", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said. ")
            text_to_speech("Sorry, could not understand what you said. ")
            # return ""
        except sr.RequestError as e:
            print("Some error processing the audio", str(e))
            # return ""
        

if __name__ == "__main__":
    speech_to_text()


