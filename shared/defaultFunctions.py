from shared.logger import logger
def splitForCommand(input):
    import re
    logger.debug(f'splitting input: {input}')
    split_command = re.findall(r'(?:[^\s,"\']|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')+', input)
    logger.debug(f'splitted output: {split_command}')
    return split_command

def stripQuotesFromArray(split_command):
    logger.debug(f'stripping quotes from input: {split_command}')
    split_command = [word.strip("'\"") for word in split_command]
    logger.debug(f'stripped output: {split_command}')
    return split_command

def getCommandsDict():
    import model.preset as preset
    import shared.defaultFunctions as defaultFunctions
    import shared.setup as setup
    commands = {}
    defaultData = setup.readJson("configuration/defaultData.json")
    defaultCommand = defaultData["defaultCommands"]
    commands.update(defaultCommand)
    commands.update(preset.getCommands())
    return commands

def maxLength(text, amount = 40):
    if len(text) > amount:
        return text[:amount] + "..."
    else:
        return text