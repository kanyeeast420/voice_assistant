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

# initialize AI Voice
engine = pyttsx3.init()

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


# open new browser tab with url


def openURL(url):
    # announce action
    callAction("Openning {0}".format(url))

    # open browser
    sleep(1)
    webbrowser.open_new_tab("https://{0}/".format(url))

# get a wikipedia page summary by query


def searchWiki(query):
    # announce action
    callAction("Searching wiki for {0}".format(query))

    # search wikipedia api for summary
    page = wikipedia.page(query)
    print("\n" + bg.blue + page.title + bg.rs +
          " - " + page.url + "\n\n" + page.summary)

# search github api for all repos of a specific org


def get_repositories_from_organization(org):
    # announce action
    callAction("Searching Github repositories from {0}".format(org))

    # search api for repositories
    url = "https://api.github.com/orgs/" + org + "/repos"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    print([repo["name"] for repo in data])

# calculate math problem


def calculate(query, operator):
    # announce action
    callAction("Calculating {0}".format(query))


# get the lyrics of a song with artist


def getLyrics(song, artist):
    # announce action
    callAction("Displaying lyrics for {0}".format(song))

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


# actions for assistant


def functions(output):
    if "open" in output:
        url = str(output).replace("open ", "")
        openURL(url=url)

    if "what is" in output:
        query = str(output).replace("what is ", "")
        searchWiki(query=query)

    if "get repositories" in output:
        orga = str(output).replace("get repositories ", "")
        get_repositories_from_organization(org=orga)

    if "get lyrics" in output:
        meta = str(output).replace("get lyrics ", "")
        end = meta.split(" by ")
        print(bg.blue + str(end) + bg.rs + "\n\n")
        getLyrics(song=str(end[0]), artist=str(end[1]))

    if "get the latest crypto" in output:
        value = str(output).replace("get the latest crypto ", "")
        getTopStocks(query=value)
