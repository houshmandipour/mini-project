from gtts.tts import gTTS
from playsound import playsound

def text_to_speech():
    while True:
        message = input("Enter message: ")
        speech = gTTS(text=message)
        speech.save("DataFlair.mp3")
        playsound("DataFlair.mp3")
        log_out= input("do you wan't exit? (y=yes, n=no)")
        if log_out == "n":
            exit() 
text_to_speech()
