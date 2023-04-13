from shared.logger import logger
import handlers.textHandler as textHandler

defaultPresetData = {
    "loop": 0,
    "commands": {},
    "settings": {
        "activeEffects": ["henk"],
    },
    "memory": {},
    "effects": {
        "henk": {
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
                "a": "b",
            },
        },
    }
}

class Preset:
    """
    A brief description of what the class does.
    """
    import uuid
    
    def __init__(self, nickname="user", presetName="default", presetID=uuid.uuid4(), presetData=defaultPresetData):
        self.nick = nickname
        self.presetName = presetName
        self.Id = presetID
        self.data = presetData
        
        logger.debug(f'created Preset: {self.presetName} with ID: {self.Id} and nickname: {self.nick}')
    
    def method1(self, arg3):
        """
        A brief description of what method1 does.

        :param arg3: A description of the third argument.
        :return: A description of what the method returns.
        """
        # implementation here
    
    def method2(self):
        """
        A brief description of what method2 does.

        :return: A description of what the method returns.
        """
        # implementation here

class PresetHandler:

    
    def __init__(self, data={}):
        self.data = data
        
        logger.debug(f'created PresetHandler')
    
    def method1(self, arg3):
        """
        A brief description of what method1 does.

        :param arg3: A description of the third argument.
        :return: A description of what the method returns.
        """
        # implementation here
    
    def method2(self):
        """
        A brief description of what method2 does.

        :return: A description of what the method returns.
        """
        # implementation here

currentPreset = Preset()
handler = PresetHandler()

def getPreset():
    global currentPreset
    logger.debug(f'getPreset called, returning: {currentPreset.presetName}')
    return currentPreset.presetName

def savePreset(chatEffect, feedback=True):
    textHandler.textController(f"Preset save placeholder", chatEffect=chatEffect, feedback=feedback)

def loadPreset(presetName, chatEffect, feedback=True):
    textHandler.textController(f"Preset load placeholder", chatEffect=chatEffect, feedback=feedback)

def setName(name, chatEffect, feedback=True):
    global currentPreset
    currentPreset.presetName = name
    logger.info(f'Preset name set to: {currentPreset.presetName}')
    textHandler.textController(f"Preset name set to: {currentPreset.presetName}", chatEffect=chatEffect, feedback=feedback)
    return currentPreset.presetName

def getCommands():
    logger.debug(f'getCommands called, returning: {currentPreset.data["commands"]}')
    commands = currentPreset.data["commands"]
    return commands

def getPresetData():
    logger.debug(f'getPresetData called')
    return currentPreset.data

def setPresetData(data):
    currentPreset.data = data
    logger.debug(f'setPresetData called')
    return True