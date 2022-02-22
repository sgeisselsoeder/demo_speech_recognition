# sudo apt install espeak
import pyttsx3

engine = pyttsx3.init()
# engine = pyttsx3.init('sapi5') windows only
# voices = engine.getProperty('voices')
# for voice in voices:
#     print(f'{voice.name} {voice.gender}')
# engine.setProperty('voice', voices[1].id)

# best settings with linux default voices
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate', 98)

engine.say("Hello World how are you?")
engine.runAndWait()
engine.stop()
