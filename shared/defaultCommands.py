from shared.logger import logger
import shared.defaultFunctions as defaultFunctions
import models.preset as preset
import handlers.textHandler as textHandler
import handlers.importHandler as importHandler
import shared.appData as appData

def getInfoFromCommand(command, parameters = False, categories = False, defaultParameters = False):
    logger.debug(f'getInfoFromCommand called: {command}, {parameters}, {categories}')
    description = ""
    data = {}
    category = []
    if (command in defaultFunctions.getCommandsDict()):
        if "description" in defaultFunctions.getCommandsDict()[command]:
            description = defaultFunctions.getCommandsDict()[command]["description"]
        if "parameters" in defaultFunctions.getCommandsDict()[command]:
            data = defaultFunctions.getCommandsDict()[command]["parameters"]
        if "category" in defaultFunctions.getCommandsDict()[command]:
            category = defaultFunctions.getCommandsDict()[command]["category"]
    returnText = ''
    if (description != ""):
        returnText += f'The description: \'{description}\'\n'
    else:
        returnText += f'The command has no description\n'
    if (parameters):
        if len(data) == 0:
            returnText += f'The \"{command}\" command has no parameters\n'
        else:
            returnText += f'The parameters of the \"{command}\" command are:\n\n'
            for key in list(data.keys()):
                if ("description" in data[key] and data[key]["description"] != ""):
                    returnText += f'    {data[key]["given"]}: {data[key]["description"]}\n'
                else:
                    returnText += f'    {data[key]["given"]}: No description\n'
                if defaultParameters:
                    returnText += f'    Default value: {data[key]["default"]}\n'
                    if "options" in data[key] and len(data[key]["options"]) > 0:
                        returnText += f'    Other default options:\n'
                        for item in data[key]["options"]:
                            if item != data[key]["default"]:
                                returnText += f'        {item}\n'
                        
    if (categories):
        if len(category) == 0:
            returnText += f'The \"{command}\" command has no categories\n'
        else:
            returnText += f'Has these categories: \n'
            for item in category:
                returnText += f'\'{item}\', '
            returnText = returnText[:-2]
    return returnText
    
def listCommands(filerCategory = '', maxCharacters: int = 40):
    logger.debug(f'listCommands called')
    if (filerCategory != ''):
        returnText = f'The commands with the filter "{filerCategory}" are:\n'
    else:
        returnText = 'The commands are:\n'
    for key in list(defaultFunctions.getCommandsDict().keys()):
        if (filerCategory == '' or filerCategory in defaultFunctions.getCommandsDict()[key]["category"]):
            if "description" in defaultFunctions.getCommandsDict()[key]:
                returnText += f'    {key}: {defaultFunctions.maxLength(defaultFunctions.getCommandsDict()[key]["description"], maxCharacters)}\n'
            else:
                returnText += f'    {key}: No description\n'
    if (returnText == 'The commands are:\n'):
        returnText = f'No commands found with filter "{filerCategory}"'
    return returnText   

def listCategories():
    logger.debug(f'listCategories called')
    returnText = 'The categories are:\n'
    for key in list(defaultFunctions.getCommandsDict().keys()):
        if "category" in defaultFunctions.getCommandsDict()[key]:
            for item in defaultFunctions.getCommandsDict()[key]["category"]:
                if item not in returnText:
                    returnText += f'    {item}\n'
    if (returnText == 'The categories are:\n'):
        returnText = 'No categories found'
    return returnText

def getCommandData(command):
    logger.debug(f'getCommandData called: {command}')
    if (command in defaultFunctions.getCommandsDict()):
        return defaultFunctions.getCommandsDict()[command]
    else:
        return False
    
def loadDefaultCommands(force, overwrite, chatEffect1, feedback = True):
    import setup as setup
    logger.debug(f'command called: {force}, {overwrite}')
    if (overwrite == True):
        text = "Are you sure you want to overwrite the current default commands? (y/n)"
    else:
        text = "Are you sure you want to reload the current default commands? (y/n)"
    if (force != True):
        textHandler.textController(text, chatEffect=chatEffect1, feedback=feedback)
        confirm = input()
        if overwrite == True:
            logger.warning(f'overwritten defaultCommands.json with hardcoded default commands')
        if (force == True or confirm.lower() == "y"):
            return setup.createJsonIfNotExists("configuration/defaultCommands.json", setup.defaultCommands, overwrite)
    else:
        if overwrite == True:
            logger.warning(f'overwritten defaultCommands.json with hardcoded default commands')
        return setup.createJsonIfNotExists("configuration/defaultCommands.json", setup.defaultCommands, overwrite)
    
def formatMetaData(metaData = False):
    if metaData == False:
        return "There was no metaData found"
    elif metaData == [0]:
        return "Unknown type"
    else:
        value = "MetaData:\n"
        for key in list(metaData.keys()):
            if metaData[key] != "":
                value += "    " + key + ": " + metaData[key] + "\n"
        if value == "MetaData:\n":
            value = "There was no metaData found"
        return value

def getMetaData(name, typeOfData):
    data = False
    match typeOfData:
        case "command":
            if (name in defaultFunctions.getCommandsDict()):
                data = defaultFunctions.getCommandsDict()[name]
        case "preset":
            if (name in preset.handler.getPresets()):
                data = preset.handler.getPresetData(name)
        case "library":
            if (name in importHandler.getLibraries()):
                data = importHandler.getLibraryData(name)
        case "program":
            return appData.metaData
        case _:
            # get dialog: "unknown type" "not found" which it gets with a normal False
            return [0]
    logger.debug(f'getMetaData called: {name}, {typeOfData}, data: {data}')
    if type(data) == type({}) and "metaData" in data:
        return data["metaData"]
    else:
        return False
    
