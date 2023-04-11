from shared.logger import logger
import shared.defaultFunctions as defaultFunctions
import model.preset as preset
import handlers.textHandling as textHandling

def getInfoFromCommand(command, parameters = False):
    logger.debug(f'getInfoFromCommand called: {command}, {parameters}')
    description = ""
    data = {}
    if (command in defaultFunctions.getCommandsDict()):
        description = defaultFunctions.getCommandsDict()[command]["description"]
        if "parameters" in defaultFunctions.getCommandsDict()[command]:
            data = defaultFunctions.getCommandsDict()[command]["parameters"]
    returnText = ''
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
    else :
        returnText = description
    return returnText
    
def listCommands():
    logger.debug(f'listCommands called')
    returnText = 'The commands are:\n'
    for key in list(defaultFunctions.getCommandsDict().keys()):
        if "description" in defaultFunctions.getCommandsDict()[key]:
            returnText += f'{key}: {defaultFunctions.maxLength(defaultFunctions.getCommandsDict()[key]["description"])}\n'
        else:
            returnText += f'{key}: No description\n'
    return returnText   