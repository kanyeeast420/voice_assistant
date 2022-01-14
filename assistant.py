import speech_recognition as sr
import utils.Utils as Utils
import pyttsx3
from sty import bg, fg


# initialize AI Voice
engine = pyttsx3.init()

# initialize Recorder
recognizer = sr.Recognizer()


class assistant():

    def speechToText():

        with sr.Microphone() as source:
            print("Adjusting noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # record microphone for 5 seconds
            print("Recording for 5 seconds")
            recorded_audio = recognizer.listen(source, timeout=5)
            print("Done recording\n")

        try:
            # convert to text
            print("Recognizing text\n")
            output = recognizer.recognize_google(
                recorded_audio, language="en-US")

            print("\n" + bg.green + fg.black + output + bg.rs + fg.rs + "\n")

            # functions
            Utils.functions(output=output)

        except Exception as ex:
            print(ex)


assistant.speechToText()
