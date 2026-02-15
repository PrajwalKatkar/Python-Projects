import speech_recognition as sr
import webbrowser 
import pyttsx3 
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Initializing Jarvis.......")
    while True:
        #listen for wake word jarvis

        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            command=r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Sphinx error; {0}".format(e))
