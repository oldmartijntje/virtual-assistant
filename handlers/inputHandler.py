from shared.logger import logger
import shared.defaultFunctions as defaultFunctions
import shared.defaultCommands as defaultCommands
import model.preset as preset
import shared.setup as setup
import handlers.textHandling as textHandling

def givenInput(input):
    logger.debug(f'givenInput called: {input}')
    splittedCommand = defaultFunctions.stripQuotesFromArray(defaultFunctions.splitForCommand(input))
    defaultCommand = defaultFunctions.getCommandsDict()
    if (splittedCommand[0] in defaultCommand):
        parameters = {}
        emptyParams = []
        if "parameters" in defaultCommand[splittedCommand[0]]:
            for param_name, param_info in defaultCommand[splittedCommand[0]]["parameters"].items():
                if param_info["given"] in splittedCommand and splittedCommand.index(param_info["given"]) + 1 < len(splittedCommand):
                    given_value_index = splittedCommand.index(param_info["given"]) + 1
                    parameters[param_name] = splittedCommand[given_value_index]
                    splittedCommand.pop(given_value_index)
                    splittedCommand.pop(given_value_index -1)
                else:
                    emptyParams.append(param_name)
            logger.debug(f'params needed: {emptyParams}')
            if len(emptyParams) > 0 and len(defaultCommand[splittedCommand[0]]["parameters"]) > 0:
                loop = 0
                for item in splittedCommand:
                    loop +=1
                    if loop == 1:
                        pass
                    elif len(emptyParams) > 0 and len(defaultCommand[splittedCommand[0]]["parameters"]) > 0:
                        parameters[emptyParams[0]] = item
                        emptyParams.pop(0)
                if len(emptyParams) > 0:
                    for item in emptyParams:
                        parameters[item] = defaultCommand[splittedCommand[0]]["parameters"][item]["default"]


            function = defaultCommand[splittedCommand[0]]["function"].format(*defaultFunctions.dictToList(parameters, defaultCommand[splittedCommand[0]]["parameters"]))
            logger.debug(f'given value: {function}')
            
        else:
            function = defaultCommand[splittedCommand[0]]["function"]
        logger.debug(f'func: {function}')
        try:
            exec(function)
        except Exception as e:
            logger.error(f'Error: {e}')
            textHandling.textController(f'Error: {e}')

    

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
    


    