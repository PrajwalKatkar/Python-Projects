import speech_recognition as sr
import webbrowser 
import pyttsx3 
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine=pyttsx3.init()
def processcommand(c):
    pass
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing Jarvis.......")
    while True:
        #listen for wake word jarvis

        # obtain audio from the microphone
        r = sr.Recognizer()
    

        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processcommand()
        except Exception as e:
            print("Sphinx error; {0}".format(e))
