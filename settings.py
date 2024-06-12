import json

def loadSettings():
    with open("settings.json", "r") as file:
        return json.load(file)

playerSettings = loadSettings()
