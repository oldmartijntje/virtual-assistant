from shared.logger import logger
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

currentPreset = Preset()

def getPreset():
    global currentPreset
    logger.debug(f'getPreset called, returning: {currentPreset.presetName}')
    return currentPreset.presetName

def savePreset():
    pass

def loadPreset(presetName):
    pass