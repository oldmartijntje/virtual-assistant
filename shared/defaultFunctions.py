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
    import models.preset as preset
    import setup as setup
    commands = {}
    defaultCommand = setup.readJson("configuration/defaultCommands.json")
    if defaultCommand == False:
        setup.createJsonIfNotExists("configuration/defaultCommands.json", {})
        defaultCommand = setup.defaultCommands
    commands.update(setup.failsafeCommands)
    commands.update(defaultCommand)
    activeTestingSettings = setup.readJson("debug/testingSettings.json", False)
    if activeTestingSettings != False and activeTestingSettings["testing"] == True:
        commands.update(setup.testingCommands)
    commands.update(preset.getCommands())
    return commands

def maxLength(text, amount = 40):
    if len(text) > amount:
        return text[:amount] + "..."
    else:
        return text
    
def dictToList(dictionary, order):
    logger.debug(f'ordering: {dictionary.values()}')
    returnList = list(dictionary.values())
    returnListKeys = list(dictionary.keys())
    returnListInOrder = []
    order = list(order.keys())
    for item in order:
        for key in returnListKeys:
            if key == item:
                returnListInOrder.append(dictionary[key])
                logger.debug(f'order: {returnListInOrder}')
    return returnListInOrder

def encodeToHex(text):
    import codecs
    return codecs.encode(text.encode(), 'hex').decode()

def createCommand(name, function, parameters = []):
    import setup as setup
    import models.preset as preset
    defaultCommand = setup.readJson("configuration/defaultCommands.json")
    if defaultCommand == False:
        setup.createJsonIfNotExists("configuration/defaultCommands.json", {})
        defaultCommand = setup.defaultCommands
    defaultCommand[name] = {"function": function, "parameters": parameters}
    setup.writeJson("configuration/defaultCommands.json", defaultCommand)
    preset.currentPreset.data["commands"] = defaultCommand
    preset.savePreset()

def hide_ip_address(ip_address):
    # Split the IP address into four octets
    octets = str(ip_address).split('.')
    
    # Replace the second and third octets with asterisks
    octets[1:3] = ['*' * len(octets[1]), '*' * len(octets[2])]
    
    # Join the octets back together with dots and return the masked IP address
    return '.'.join(octets)