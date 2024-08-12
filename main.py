import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text) :
    ttsx.say(text)
    ttsx.runAndWait()


if __name__ == "__main__" :
    speak("Initializing Jarvis....")

    while True:

        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone

        r = sr.Recognizer()
        print("Recoginizing.......")

        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
        
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Error ; {0}".format(e))