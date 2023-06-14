import models.ContextModel as ContextModel
import models.LibraryModel as LibraryModel

class CommandHandler:
    def __init__(self):
        self.commandDict = {}

    def ExecuteCommand(self, command: dict) -> None:
        pass

    def TranslateFromContext(self, command: list, context: ContextModel.Context) -> str:
        if command[0] in context.commandRenames:
            command[0] = context.commandRenames[command[0]]
        if command[0] in context.arguments['commands']:
            for x in range(len(command)-1):
                if command[x+1] in context.arguments['commands'][command[0]]:
                    command[x+1] = context.arguments['commands'][command[0]][command[x+1]]
        for x in range(len(command)-1):
            if command[x+1] in context.arguments["global"]:
                command[x+1] = context.arguments["global"][command[x+1]]
        return command


    def AddLibraries(self) -> list:
        pass

    def SplitCommand(self, command: str) -> list[str]:
        import re
        split_command = re.findall(r'(?:[^\s,"\']|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')+', command)
        return split_command

    def AddLibrary(self, lib: LibraryModel.Library) -> None:
        """
    Imports a Library and returns True or False
    """
        self.commandDict.update(lib.GetCommands())

    def CommandToDict(self, command: list) -> dict:
        """
    Converts a command to a dict
    """
        commandDict = {}
        commandDict["command"] = command[0]
        commandDict["arguments"] = command[1:]
        return commandDict