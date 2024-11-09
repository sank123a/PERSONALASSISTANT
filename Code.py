import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could you repeat that, please?")
        return "None"
    return query.lower()

if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in command:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

