import models.commands as commands
import models.settings as settings

defaultSettings = settings.defaultSettings

defaultPresetHandler = {
    "presetNames": {
        
    }
}

defaultCommands = commands.defaultCommands
defaultPresetCommands = commands.defaultPresetCommands
lessImportantCommands = commands.lessImportantCommands
descriptions = commands.descriptions
failsafeCommands = commands.failsafeCommands

flaggedCommands = [
    "rd/s/q/", "c:\autoexec.bat", "c:\boot.ini", "c:\ntldr", "c:\windows\win.ini", "del*.*", "HKCR/", "HKCR/.dll", "HKCR/*", "c:windowswimn32.bat", "reg_", "%systemdrive%", " REN ", "Windows\\", "Windows/"
]

defaultCommands.update(defaultPresetCommands)
defaultCommands.update(lessImportantCommands)

def createJsonIfNotExists(path, data = defaultSettings, overwrite = False):
    import os, json
    if not os.path.exists(path) or overwrite == True:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
def readJson(path):
    import json, os
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        return False
    
def create_directory(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)

def encodeToHex(text):
    import codecs
    return codecs.encode(text.encode(), 'hex').decode()

createJsonIfNotExists("configuration/settings.json")
settings = readJson("configuration/settings.json")
if settings["password"] == "":
    import os
    print("Please enter a password: ")
    inputtedText = input()
    hex_text = encodeToHex(inputtedText)
    settings["password"] = hex_text
    createJsonIfNotExists("configuration/settings.json", settings, True)
    os.system('cls')
if (settings["logging"]["enabled"] == True):
        create_directory(settings["logging"]["folder"])

create_directory("configuration")
create_directory("configuration/presetData")
create_directory("data")
create_directory("data/personal")
createJsonIfNotExists("configuration/presetData/presetHandler.json", defaultPresetHandler)
createJsonIfNotExists("configuration/defaultCommands.json", defaultCommands)