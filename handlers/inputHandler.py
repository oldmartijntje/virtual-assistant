from shared.logger import logger
defaultCommand= {
    "exit": {
        "description": "Exits the program",
        "function": 'exit()',
        "parameters": {}
    },
    "print": {
        "description": "Prints the given text",
        "function": 'print({})',
        "parameters": {"var1": {"default": "'Hello World!'", "given": "-name"}}
    },
    "test": {
        "description": "Test command",
        "function": 'print({}, {})',
        "parameters": {"var1": {"default": "'Hello'", "given": "-name"},
                       "var2": {"default": "'World!'", "given": "-desc"}
        }
    }
}

def givenInput(input):
    import model.preset as preset
    import handlers.textHandling as textHandling
    splittedCommand = splitForCommand(input)

    if (splittedCommand[0] in defaultCommand):
        parameters = []
        for param_name, param_info in defaultCommand[splittedCommand[0]]["parameters"].items():
            if param_info["given"] in splittedCommand and splittedCommand.index(param_info["given"]) + 1 < len(splittedCommand):
                given_value_index = splittedCommand.index(param_info["given"]) + 1
                parameters.append(splittedCommand[given_value_index])
            else:
                parameters.append(param_info["default"])
        function = defaultCommand[splittedCommand[0]]["function"].format(*parameters)
        exec(function)

    # logger.debug(f'givenInput called: {input}')
    # if (input == "exit"):
    #     exit()
    # elif (input == "pc user"):
    #     import os
    #     textHandling.textController("Current user: " + str(os.getlogin()))
    # elif (input == "preset"):
    #     textHandling.textController("Current preset: " + str(preset.getPreset()))
    # elif ("preset -set name" in input):
    #     preset.setName(input.split("preset -set name ")[1])
    # elif ("preset -save" in input):
    #     preset.savePreset()
    # elif ("preset -load" in input):
    #     preset.loadPreset(input.split("preset -load ")[1])
    # elif ("preset" in input and "help" in input):
    #     textHandling.textController("'preset' to display preset name\n'preset -set name <name>' to set the preset name\n'preset -save' to save the preset to file\n'preset -load <name>' to load the preset from file\n'preset -help' to display this message")
    # elif ("help" in input):
    #     textHandling.textController("'exit' to exit the program\n'pc' pc commands\n'preset' preset stuff\n'help' to display this message\n\nput -help after a command to display more info about it")
    # elif (input=="cmd"):
    #     import os
    #     os.system("cmd")
    # elif ("cmd -r" in input):
    #     import os
    #     os.system("cmd /k " + input.split("cmd -r ")[1])
    # else:
    #     textHandling.textController("Invalid input")
    #     return False
    
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