import speech_recognition as sr
# import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text):
    print(text)
    # engine.say(text)


def get_command():
    try:
        with sr.Microphone() as source:
            print("I am listening ... what you say now will be sent to Google by default!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            searchstring = "computer"
            if searchstring in command:
                # print(searchstring + " was mentioned! Removing it.")
                command = command.replace(searchstring, "")
            else:
                command = None
    except Exception as e:
        print(e)
        return None
    return command


def run():
    command = get_command()
    if command is None:
        return False

    if 'play' in command:
        song = command.replace("play", "")
        print("Song to play is" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        timestring = 'Current time is ' + time
        talk(timestring)

    elif 'wikipedia' in command:
        person = command.replace("wikipedia", "")
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'alive' in command:
        talk("I might be alive one day ...")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'shut down' in command:
        talk("It was a pleasure talking to you")
        return True

    else:
        talk("Sorry, I don't know what to do! Please repeat")
    return False


while True:
    shutdown = run()
    if shutdown:
        break
