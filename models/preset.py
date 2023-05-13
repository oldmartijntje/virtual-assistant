from shared.logger import logger
import handlers.textHandler as textHandler

defaultPresetData = {
    "loop": 0,
    "commands": {},
    "exitCommands": [
        "print -txt \"Goodby!\""
    ],
    "settings": {
        "activeEffects": [],
        "autoSave": False,
        "editWithoutPassword": True,

    },
    "memory": {},
    "effects": {
        "testing": {
            "commands": {
                "beforeText": ["print beforeText", "print beforeText2"],
                "afterText": ["print afterText", "print afterText2"],
            },
            "text": {
                "beforeText": "beforeText",
                "afterText": "afterText",
            },
            "replaceText": {
                "1": "2",
                "a": "-MEOW-",
            },
            "runTextInCommands": ["print \"meow - {}\""],
            "feedback": True
        },
    },
    "metaData": {
        "name": "Default",
        "author": "OldMartijntje",
        "version": "1.0.0",
        "description": "Default preset."
    },
    "self": {
        "nick": "user",
        "presetName": "Default",
        "Id": "00000000-0000-0000-0000-000000000000",
        "nameHistory": []
    }
}
# only the last effect in the list will be checked for "feedback": False

class Preset:
    """
    A brief description of what the class does.
    """
    import uuid
    
    def __init__(self, nickname="user", presetName="Default", presetID=str(uuid.uuid4()), presetData=defaultPresetData):
        self.nick = nickname
        self.presetName = presetName
        self.Id = presetID
        self.data = presetData
        self.data["self"]["nick"] = self.nick
        self.data["self"]["presetName"] = self.presetName
        self.data["self"]["Id"] = self.Id
        self.data["self"]["nameHistory"] = [self.presetName]
        
        logger.debug(f'created Preset: {self.presetName} with ID: {self.Id} and nickname: {self.nick}')
    
    def changeMetaData(self, name, author, version, description):
        if name != "":
            self.data["metaData"]["name"] = name
        if author != "":
            self.data["metaData"]["author"] = author
        if version != "":
            self.data["metaData"]["version"] = version
        if description != "":
            self.data["metaData"]["description"] = description
        logger.info(f'changed metaData of {self.Id} preset to: {self.data["metaData"]}')

    
    def getActiveEffects(self):
        return self.data["settings"]["activeEffects"]
    
    def setActiveEffect(self, effect):
        self.data["settings"]["activeEffects"].append(effect)
        logger.info(f'added {effect} to activeEffects of {self.Id} preset')

    def removeActiveEffect(self, effect):
        self.data["settings"]["activeEffects"].remove(effect)
        logger.info(f'removed {effect} from activeEffects of {self.Id} preset')

    def createEffect(self, effectName, effectData):
        import setup
        default = {"commands": {}, "text": {}, "replaceText": {}, "runTextInCommands": [], "feedback": True}
        if effectData != '':
            data = setup.readJson(effectData, False)
            if data != False:
                effectData = data
            else:
                return 'JSON file doesn\'t exist'
            for item in default.keys():
                if item not in effectData.keys():
                    effectData[item] = default[item]
        else:
            effectData = default
        if effectName in self.data["effects"].keys():
            logger.error(f'effect {effectName} already exists in {self.Id} preset')
            return f'effect {effectName} already exists in {self.Id} preset'

            
        self.data["effects"][effectName] = effectData
        logger.info(f'created {effectName} effect in {self.Id} preset')
        return True
    
    def getEffectList(self):
        return list(self.data["effects"].keys())

    def savePresetToFile(self):
        global handler
        import setup
        self.data["self"]["presetName"] = self.presetName
        handler.changePresetName(self.Id, self.presetName, self.data["self"]["nameHistory"][0])
        self.data["self"]["nameHistory"] = [self.presetName]
        setup.createJsonIfNotExists(f"configuration/presetData/preset{self.Id}.json", self.data, True)
        logger.info(f'saved {self.Id} preset to file')

    def loadPresetFromFile(self, id):
        import setup
        data = setup.readJson(f"configuration/presetData/preset{id}.json")
        if data == False:
            return False
        else:
            self.data = data
            self.Id = id
            self.presetName = self.data["self"]["presetName"]
            self.nick = self.data["self"]["nick"]
            logger.info(f'loaded {self.Id} preset from file')
            return True

class PresetHandler:
    def __init__(self, data={}):
        self.data = data
        self.storage = "configuration/presetData/presetHandler.json"
        
        logger.debug(f'created PresetHandler')
    
    def importData(self):
        import setup
        self.data = setup.readJson(self.storage)
        logger.debug(f'imported data from: {self.storage}')
        settings = setup.readJson("configuration/settings.json")
        if settings["preferences"]["anonymous"] == True:
            settings["preferences"]["username"] = "Anonymous"
        if self.data == {} or self.data == False:
            logger.debug(f'imported data was empty, creating default data')
            self.data = {
                "presetNames": {},
                "packages": {},
                "metaData": {
                    "name": "PresetHandler",
                    "author": settings["preferences"]["username"],
                    "version": "1.0.0",
                    "description": "The Autogenerated Default presetHandler."
                },
            }
            self.exportData()
    
    def exportData(self):
        import setup
        setup.createJsonIfNotExists(self.storage, self.data, True)
        logger.debug(f'exported data to: {self.storage}')

    def find_by_name(self, substring):
        matching_items = []
        for key in self.data['presetNames'].keys():
            if substring in key:
                matching_items += self.data['presetNames'][key]
        return matching_items
    
    def getMetaDataById(self, presetId):
        import setup
        logger.debug(f'getPresetMetaData called w presetId: "{presetId}"')
        if presetId in self.data["packages"]:
            return self.data["packages"][presetId]["metaData"]
        else:
            data = setup.readJson(f"configuration/presetData/preset{presetId}.json")
            if data == False:
                return False
            if "metaData" in data:
                return data["metaData"]
            return ['No metaData found']
        
    def getPresetNameById(self, presetId):
        import setup
        logger.debug(f'getPresetNameById called w presetId: "{presetId}"')
        if presetId in self.data["packages"]:
            return self.data["packages"][presetId]["self"]["presetName"]
        else:
            data = setup.readJson(f"configuration/presetData/preset{presetId}.json")
            if data == False:
                return False
            if "self" in data:
                return data["self"]["presetName"]
            return ['No presetName found']
        
    
    def getPresetById(self, presetId):
        import setup
        logger.debug(f'getPresetById called w presetId: "{presetId}"')
        return setup.readJson(f"configuration/presetData/preset{presetId}.json")
    
    def changePresetName(self, presetId, newName, oldName):
        logger.debug(f'changePresetName called w presetId: "{presetId}", newName: "{newName}", oldName: "{oldName}"')
        if newName == oldName:
            return
        if newName in self.data["presetNames"]:
            self.data["presetNames"][newName].append(presetId)
        else:
            self.data["presetNames"][newName] = [presetId]
        if oldName in self.data["presetNames"] and presetId in self.data["presetNames"][oldName]:
            self.data["presetNames"][oldName].remove(presetId)
        if oldName in self.data["presetNames"] and len(self.data["presetNames"][oldName]) == 0:
            del self.data["presetNames"][oldName]
        self.exportData()


currentPreset = Preset()
handler = PresetHandler()
handler.importData()

def getPreset():
    global currentPreset
    logger.debug(f'getPreset called, returning: {currentPreset.presetName}')
    return currentPreset.presetName

def savePreset(chatEffect, feedback=True):
    global currentPreset
    currentPreset.savePresetToFile()
    textHandler.textController(f"Preset saved", chatEffect=chatEffect, feedback=feedback)

def loadPreset(presetId, chatEffect, feedback=True):
    if currentPreset.loadPresetFromFile(presetId):
        textHandler.textController(f"Preset loaded", chatEffect=chatEffect, feedback=feedback)
    else:
        textHandler.textController(f"Preset not found", chatEffect=chatEffect, feedback=feedback)

def getListOfPresetsByName(filterText):
    global handler
    logger.debug(f'getListOfPresets called')
    return handler.find_by_name(filterText)

def setName(name, chatEffect, feedback=True):
    global currentPreset
    currentPreset.presetName = name
    logger.info(f'Preset name set to: {currentPreset.presetName}')
    textHandler.textController(f"Preset name set to: {currentPreset.presetName}", chatEffect=chatEffect, feedback=feedback)
    return currentPreset.presetName

def getCommands():
    logger.debug(f'getCommands called of preset: {currentPreset.presetName}')
    commands = currentPreset.data["commands"]
    return commands

def getPresetData():
    logger.debug(f'getPresetData called')
    return currentPreset.data

def setPresetData(data):
    currentPreset.data = data
    logger.debug(f'setPresetData called')
    return True

def debug():
    logger.debug(f'preset debug called')
    return True

def getMetaDataById(presetId):
    return handler.getMetaDataById(presetId)

def getFormattedMetaDataById(presetId):
    metaData = getMetaDataById(presetId)
    name = handler.getPresetNameById(presetId)
    nameText = ""
    if name == False:
        nameText = "No name found"
    else:
        nameText = f"'{name}'"
    if metaData == False:
        return f"-Preset: '{presetId}'\n   404 Not found"
    if type(metaData) == list:
        return f"-Preset: '{presetId}'\n   FilterName: {nameText}\n   {metaData[0]}"
    return f"-Preset: {presetId}\n   FilterName: {nameText}\n   Metadata name: '{metaData['name']}' by {metaData['author']}\n   {metaData['description']}"

def getFormattedPresetList(filterText):
    if filterText == 'True':
        filterText = ""
    text = ""
    presetList = getListOfPresetsByName(filterText)
    for preset in presetList:
        text += getFormattedMetaDataById(preset) + "\n"
    return text

def getActiveEffect():
    logger.debug(f'getActiveEffects called')
    return currentPreset.getActiveEffects()

def setActiveEffect(effect):
    logger.debug(f'setActiveEffects called')
    return currentPreset.setActiveEffect(effect)

def removeActiveEffect(effect):
    logger.debug(f'removeActiveEffects called')
    return currentPreset.removeActiveEffect(effect)

def createEffect(name, json, chatEffect=True, feedback=True):
    logger.debug(f'createEffect called')
    created = currentPreset.createEffect(name, json)
    if created == True:
        textHandler.textController(f"Effect created", chatEffect=chatEffect, feedback=feedback)
    else:
        textHandler.textController(f"{created}", chatEffect=chatEffect, feedback=feedback)

def getEffectList(chatEffect=True, feedback=True):
    logger.debug(f'getEffectList called')
    textHandler.textController(currentPreset.getEffectList(), chatEffect=chatEffect, feedback=feedback)