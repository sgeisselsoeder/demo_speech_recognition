import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate', 100)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def get_command():
    command = None
    talk("listening")
    while command is None:
        try:
            with sr.Microphone() as source:
                voice = listener.listen(source)
                # raises for silence
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
                searchstring = "computer"
                if searchstring in command:
                    # print(searchstring + " was mentioned! Removing it.")
                    command = command.replace(searchstring, "")
                else:
                    print("didn't say the magic word")
                    command = None
        except sr.UnknownValueError:
            # Only analyzed silence
            # print("No recognizable words")
            print("...")
            pass
        except Exception as e:
            print("ERROR")
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

    elif 'hear me' in command:
        talk("Yes, I can hear you")

    elif 'alive' in command:
        talk("I might be alive one day ...")

    elif 'joke' in command:
        text = pyjokes.get_joke()
        talk(text)

    elif "light" in command or "licht" in command or "lamp" in command:
        keywords_off = ["off", "aus", "dunkel"]
        for keyword_off in keywords_off:
            if keyword_off in command:
                os.system("ssh pi@192.168.178.50 python /home/pi/lightoff.py")
                return
        # keywords_on = ["on", "an", "hell"]
        # for keyword_on in keywords_on:
        #     if keyword_on in command:
        os.system("ssh pi@192.168.178.50 python /home/pi/lighton.py")

    elif "dark" in command or "dunkel" in command:
        os.system("ssh pi@192.168.178.50 python /home/pi/lightoff.py")

    elif "bright" in command or "hell" in command:
        os.system("ssh pi@192.168.178.50 python /home/pi/lighton.py")

    elif 'shut down' in command:
        talk("It was a pleasure talking to you")
        return True

    else:
        talk("Please repeat")
    return False


talk("I will be listening in a second ... what you say now will be sent to Google by default!")
while True:
    shutdown = run()
    if shutdown:
        break
