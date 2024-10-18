import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again please...")
        return "None"

if __name__ == "__main__":
    while True:
        query = takeCommand()

        if "help" in query:
            speak("Panic Mode Activated!")
            print("Panic Mode Activated!")
            break  # Exits the loop after detecting "help"
        else:
            speak("No panic detected.")
            print("No panic detected.")
