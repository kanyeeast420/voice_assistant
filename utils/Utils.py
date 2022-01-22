import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3
from time import sleep
import urllib.request
import json
import os
from sty import fg, bg, ef, rs
import lyricsgenius
from dotenv import load_dotenv
import requests
import string
import random
import pyperclip

# initialize AI Voice
engine = pyttsx3.init()

# change voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

# initialize Recorder
recognizer = sr.Recognizer()

# System call
os.system("")

# enviroment variables
load_dotenv()

# initialize Genius Lyrics
genius = lyricsgenius.Genius(os.getenv("GENIUS_ACCESS_TOKEN"))

# announce any action


def callAction(call):
    engine.say(call)
    engine.runAndWait()

# open browser


def openBrowser(url):
    webbrowser.open_new_tab(f"https://{url}")

# open new browser tab with url


def openURL(url):
    # announce action
    callAction(f"Openning {url}")

    # open browser
    sleep(1)
    openBrowser(url=url)

# get a wikipedia page summary by query


def searchWiki(query):
    # announce action
    callAction(f"Searching wiki for {query}")

    # search wikipedia api for summary
    page = wikipedia.page(query)
    print("\n" + bg.blue + page.title + bg.rs +
          " - " + page.url + "\n\n" + page.summary)

# search github api for all repos of a specific org


def get_repositories_from_organization(org):
    # announce action
    callAction(f"Searching Github repositories from {org}")

    # search api for repositories
    url = "https://api.github.com/orgs/" + org + "/repos"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    print([repo["name"] for repo in data])

# calculate math problem


def calculate(query, operator):
    # announce action
    callAction(f"Calculating {query}")


# get the lyrics of a song with artist


def getLyrics(song, artist):
    # announce action
    callAction(f"Displaying lyrics for {song}")

    # find lyrics
    lyrics = genius.search_song(song, artist)
    print(lyrics.lyrics)

# get the top stocks from api


def getTopStocks(query):
    # announce action
    callAction("Fetching latest crypt")

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        "X-CMC_PRO_API_KEY": os.getenv("COIN_MARKET_CAP_TOKEN"),
        "Accepts": "application/json"
    }

    params = {
        "start": "1",
        "limit": "10",
        "convert": "EUR"
    }

    json = requests.get(url, params=params, headers=headers).json()

    coins = json["data"]

    for i in coins:
        print(i["symbol"], i["quote"]["EUR"]["price"])

# generate custom password with length


def generatePsw(length):
    # announce action
    callAction("Generating password")

    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    # generate psw
    random.shuffle(characters)

    password = []

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print(bg.blue + "{0}".format("".join(password)) + bg.rs)

    callAction("Generated password: {0}".format("".join(password)))

    pyperclip.copy("".join(password))
    callAction("\ncopied to clipboard")

# search google for anything


def searchGoogle(searchQuery):
    callAction(f"Search google for {searchQuery}")

    url = f"www.google.com/search?q={searchQuery}"

    sleep(1)
    openBrowser(url=url)

# actions for assistant


def commands(output):
    match output.split(" ")[0]:

        case "open":
            url = str(output).replace("open ", "")
            openURL(url=url)
            return "open"

        case "what":
            match output.split(" ")[1]:
                case "is" | "are":
                    query = str(output).replace("what is ", "")
                    searchWiki(query=query)
                    return "what is/are"

        case "get":
            match output.split(" ")[1]:
                case "repositories":
                    orga = str(output).replace("get repositories ", "")
                    get_repositories_from_organization(org=orga)
                    return "get repositories"
                case "lyrics":
                    meta = str(output).replace("get lyrics ", "")
                    end = meta.split(" by ")
                    print(bg.blue + str(end) + bg.rs + "\n\n")
                    getLyrics(song=str(end[0]), artist=str(end[1]))
                    return "get lyrics"

        case "generate":
            match output.split(" ")[1]:
                case "password":
                    match output.split(" ")[2]:
                        case "digits":
                            data = str(output).replace(
                                "generate password digits ", "")
                            length = int(data)
                            generatePsw(length=length)
                            return "generate password"

        case "Google":
            searchQuery = str(output).replace("Google ", "")
            searchGoogle(searchQuery=searchQuery)
            return "google"

    sleep(1)
    callAction("Please repeat, couldn't recognize a command")
    return "Error"
