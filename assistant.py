import speech_recognition as sr
import utils.Utils as Utils
import pyttsx3
from sty import bg, fg
import logging


# initialize AI Voice
engine = pyttsx3.init()

# initialize Recorder
recognizer = sr.Recognizer()

logging.basicConfig(filename="results.log",
                    encoding="utf-8", level=logging.INFO)


class assistant():

    def go():

        with sr.Microphone() as source:
            print(bg.blue + "Adjusting noise..." + bg.rs)
            recognizer.adjust_for_ambient_noise(source, duration=1)

            Utils.callAction("How can I help you?")
            # record microphone for 5 seconds
            print(bg.blue + "Recording for 7 seconds" + bg.rs)
            recorded_audio = recognizer.listen(source, timeout=7)

        try:
            # convert audio in to str
            output = recognizer.recognize_google(
                recorded_audio, language="en-US")

            print("\n" + "recognized audio: " +
                  bg.green + fg.black + output + bg.rs + fg.rs + "\n")

            # functions
            status = Utils.commands(output=output)
            # print(status)

            # create log request
            logging.info(f"Command: {status}, Input: {output}")

        except Exception as ex:
            print(ex)


assistant.go()
