from shared.logger import logger
import handlers.textHandling as textHandling
class Preset:
    """
    A brief description of what the class does.
    """
    import uuid
    
    def __init__(self, nickname="user", presetName="default", presetID=uuid.uuid4(), presetData={}):
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

def savePreset(chatEffect):
    textHandling.textController(f"Preset save placeholder", chatEffect=chatEffect)

def loadPreset(presetName, chatEffect):
    textHandling.textController(f"Preset load placeholder", chatEffect=chatEffect)

def setName(name, chatEffect):
    global currentPreset
    currentPreset.presetName = name
    logger.info(f'Preset name set to: {currentPreset.presetName}')
    textHandling.textController(f"Preset name set to: {currentPreset.presetName}", chatEffect=chatEffect)
    return currentPreset.presetName

def getCommands():
    defaultCommand= {
    }
    return defaultCommand