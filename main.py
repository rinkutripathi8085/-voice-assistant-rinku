import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language='hi-IN')
        print(f"User said: {query}")
    except:
        speak("Sorry, I didn't catch that.")
        return ""
    return query.lower()

speak("Hello, I am your voice assistant.")
while True:
    command = take_command()
    if 'time' in command or 'समय' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'open google' in command or 'गूगल खोलो' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif 'stop' in command or 'बंद करो' in command:
        speak("Thank you! Goodbye.")
        break
