import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except:
        speak("Sorry, I didn't understand.")
        return ""

def run_jarvis():
    command = take_command()

    if "hello" in command:
        speak("Hello Riya, how can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "open youtube" in command:
        speak("Opening YouTube")
        pywhatkit.playonyt("YouTube")

    elif "search" in command:
        topic = command.replace("search", "")
        info = wikipedia.summary(topic, 2)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "open google" in command:
        import webbrowser
        webbrowser.open("https://google.com")
        speak("Opening Google")

    else:
        speak("Please say the command again.")

# Main loop
speak("Jarvis is now online")

while True:
    run_jarvis()