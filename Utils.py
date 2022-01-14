import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
from time import sleep

# initialize AI Voice
engine = pyttsx3.init()

# initialize Recorder
recognizer = sr.Recognizer()

# open url in new tab


def openURL(url):

    # announce action
    engine.say("Openning {0}".format(url))
    engine.runAndWait()

    # open browser
    sleep(1)
    webbrowser.open_new_tab("https://{0}/".format(url))


def searchWiki(query):
    page = wikipedia.page(query)
    print("\n" + page.title + " - " + page.url + "\n\n" + page.summary)
