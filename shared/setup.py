defaultSettings = {"textSettings": {
    "textToSpeach": {
        "enabled": True,
    },
    "printFormat" : {
        "enabled": True,
        "defaultFormatting": {
            "start": "\033[4;3;1m",
            "end": "\033[0m"
        }
    }
}}


def createJsonIfNotExists(path, data = defaultSettings):
    import os, json
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
def readJson(path):
    import json
    with open(path, "r") as f:
        return json.load(f)