import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text) :
    ttsx.say(text)
    ttsx.runAndWait()


def processCommand(c) :
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
        
    elif "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")
        
    elif "open WhatsApp" in c.lower() :
        webbrowser.open("https://web.whatsapp.com/")

    elif "open facebook" in c.lower() :
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower() :
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play") :
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__" :
    speak("Hey Piyush, I am Your Assistant")

    while True:

        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone

        r = sr.Recognizer()
        print("Recoginizing")


        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)  
                # , timeout=2, phrase_time_limit=1

            command = r.recognize_google(audio)
            print(command)
        
            
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis") :
                speak("yes piyush")

                # Listen for command
                with sr.Microphone() as source:
                    print("I am Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)


                    processCommand(command)

        except Exception as e:
            print("Error{0}".format(e))