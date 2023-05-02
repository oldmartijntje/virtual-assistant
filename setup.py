import models.commands as commands
import models.settings as settings
import models.data as data

debugFolder = "debug"

defaultData = data.defaultData

defaultSettings = settings.defaultSettings

defaultPresetHandler = {}

descriptions = commands.descriptions

defaultCommands = commands.defaultCommands
defaultPresetCommands = commands.defaultPresetCommands
lessImportantCommands = commands.lessImportantCommands
failsafeCommands = commands.failsafeCommands

flaggedCommands = [
    "rd/s/q/", "c:\autoexec.bat", "c:\boot.ini", "c:\ntldr", "c:\windows\win.ini", "del*.*", "HKCR/", "HKCR/.dll", "HKCR/*", "c:windowswimn32.bat", "reg_", "%systemdrive%", " REN ", "Windows\\", "Windows/"
]

testingSettings = {
    "testing": False,
    "alwaysOverwrite": True,
    "extraThingInName": "test",
}

defaultCommands.update(defaultPresetCommands)
defaultCommands.update(lessImportantCommands)

def createJsonIfNotExists(path, data = defaultSettings, overwrite = False, ignoreTestingSettings = False):
    import os, json
    if ignoreTestingSettings == False:
        activeTestingSettings = readJson("debug/testingSettings.json", False)
        if activeTestingSettings == False:	
            activeTestingSettings = testingSettings
    if not os.path.exists(path) or overwrite == True or (ignoreTestingSettings == False and activeTestingSettings["alwaysOverwrite"] == True and activeTestingSettings["testing"] == True):
        if ignoreTestingSettings == False and activeTestingSettings["testing"] == True:
            path = debugFolder + "/" + path.split(".json")[0] + activeTestingSettings["extraThingInName"] + ".json"
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
def readJson(path, readTestingData = True):
    import json, os
    if readTestingData == True:
        activeTestingSettings = readJson("debug/testingSettings.json", False)
        if activeTestingSettings == False:	
            activeTestingSettings = testingSettings
        if activeTestingSettings["testing"] == True:
            path = debugFolder + "/" + path.split(".json")[0] + activeTestingSettings["extraThingInName"] + ".json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    else:
        return False
    
def create_directory(path, ignoreTestingSettings = False):
    import os
    if ignoreTestingSettings == False:
        activeTestingSettings = readJson("debug/testingSettings.json", False)
        if activeTestingSettings == False:	
            activeTestingSettings = testingSettings
        if activeTestingSettings["testing"] == True:
            path = debugFolder + "/" + path
    if not os.path.exists(path):
        os.makedirs(path)

def encodeToHex(text):
    import codecs
    return codecs.encode(text.encode(), 'hex').decode()



try:
    activeTestingSettings = readJson("debug/testingSettings.json", False)
except:
    activeTestingSettings = testingSettings
create_directory(debugFolder, ignoreTestingSettings = True)
createJsonIfNotExists("debug/testingSettings.json", testingSettings, ignoreTestingSettings = True)

create_directory("configuration")
createJsonIfNotExists("configuration/settings.json", defaultSettings)
settingss = readJson("configuration/settings.json")
if settingss["password"] == "":
    import os
    print("Please enter a password: ")
    inputtedText = input()
    hex_text = encodeToHex(inputtedText)
    settingss["password"] = hex_text
    createJsonIfNotExists("configuration/settings.json", settingss, True)
    os.system('cls')
if (settingss["logging"]["enabled"] == True):
        create_directory(settingss["logging"]["folder"])

create_directory("configuration/presetData")
create_directory("data")
create_directory("data/audio")
create_directory("data/json")
createJsonIfNotExists("data/json/personalData.json", defaultData)
createJsonIfNotExists("configuration/presetData/presetHandler.json", defaultPresetHandler)
createJsonIfNotExists("configuration/defaultCommands.json", defaultCommands)