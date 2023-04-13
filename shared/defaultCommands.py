from shared.logger import logger
import shared.defaultFunctions as defaultFunctions
import model.preset as preset
import handlers.textHandler as textHandler

def getInfoFromCommand(command, parameters = False, categories = False):
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
            returnText += f'The parameters of the \"{command}\" command are:\n'
            for key in list(data.keys()):
                if ("description" in data[key] and data[key]["description"] != ""):
                    returnText += f'{data[key]["given"]}: {data[key]["description"]}\n'
                else:
                    returnText += f'{data[key]["given"]}: No description\n'
    if (categories):
        if len(category) == 0:
            returnText += f'The \"{command}\" command has no categories\n'
        else:
            returnText += f'Has these categories: \n'
            for item in category:
                returnText += f'\'{item}\', '
            returnText = returnText[:-2]
    return returnText
    
def listCommands(filerCategory = '', maxCharacters: int = 40, listCategories: bool = False):
    logger.debug(f'listCommands called')
    if (filerCategory != ''):
        returnText = f'The commands with the filter "{filerCategory}" are:\n'
    else:
        returnText = 'The commands are:\n'
    for key in list(defaultFunctions.getCommandsDict().keys()):
        if (filerCategory == '' or filerCategory in defaultFunctions.getCommandsDict()[key]["category"]):
            if "description" in defaultFunctions.getCommandsDict()[key]:
                returnText += f'{key}: {defaultFunctions.maxLength(defaultFunctions.getCommandsDict()[key]["description"], maxCharacters)}\n'
            else:
                returnText += f'{key}: No description\n'
    if (returnText == 'The commands are:\n'):
        returnText = f'No commands found with filter "{filerCategory}"'
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