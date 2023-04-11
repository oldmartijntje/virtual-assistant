defaultSettings = {
    "textSettings": {
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
    },
    "logging": {
        "enabled": True,
        "defaultLevel": "DEBUG",
        "consoleLevel": "DEBUG",
        "fileLevel": "DEBUG",
        "folder": "logs",
        "filename": "default.log",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "filenameWithDatetimeFormatting": "VBBQD%Y-%m-%d_%H",
        "appName" : "virtualBBQduck"
    }
}

defaultPresetHandler = {
    "presetNames": {
        
    }
}

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
    
def create_directory(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)

createJsonIfNotExists("configuration/settings.json")
settings = readJson("configuration/settings.json")
if (settings["logging"]["enabled"] == True):
        create_directory(settings["logging"]["folder"])
create_directory("configuration")
create_directory("configuration/presetData")
createJsonIfNotExists("configuration/presetData/presetHandler.json", defaultPresetHandler)