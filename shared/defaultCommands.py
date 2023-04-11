from shared.logger import logger
import shared.defaultFunctions as defaultFunctions
import model.preset as preset
import handlers.textHandling as textHandling

def getInfoFromCommand(command, parameters = False, categories = False):
    logger.debug(f'getInfoFromCommand called: {command}, {parameters}')
    description = ""
    data = {}
    category = []
    if (command in defaultFunctions.getCommandsDict()):
        description = defaultFunctions.getCommandsDict()[command]["description"]
        if "parameters" in defaultFunctions.getCommandsDict()[command]:
            data = defaultFunctions.getCommandsDict()[command]["parameters"]
        if "category" in defaultFunctions.getCommandsDict()[command]:
            category = defaultFunctions.getCommandsDict()[command]["category"]
    returnText = ''
    returnText += f'The description: \'{description}\'\n'
    if (parameters):
        if len(data) == 0:
            returnText = f'The \"{command}\" command has no parameters'
        else:
            returnText = f'The parameters of the \"{command}\" command are:\n'
            for key in list(data.keys()):
                if ("description" in data[key] and data[key]["description"] != ""):
                    returnText += f'{data[key]["given"]}: {data[key]["description"]}\n'
                else:
                    returnText += f'{data[key]["given"]}: No description\n'
    if (categories):
        if len(category) == 0:
            returnText = f'The \"{command}\" command has no categories'
        else:
            returnText += f'Has these categories: \n'
            for item in category:
                returnText += f'\'{item}\', '
            returnText = returnText[:-2]
    else :
        returnText = description
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
                returnText += f'{key}: {defaultFunctions.maxLength(defaultFunctions.getCommandsDict()[key]["description"], maxCharacters)}\n'
            else:
                returnText += f'{key}: No description\n'
    if (returnText == 'The commands are:\n'):
        returnText = f'No commands found with filter "{filerCategory}"'
    return returnText   