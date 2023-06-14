import models.LibraryModel as LibraryModel
import models.CommandModel as CommandModel

class DefaultLibrary(LibraryModel.Library):
    def __init__(self):
        self.listOfCommands = []
        self.listOfCommands.append(DefaultCommand())

    def GetCommands(self) -> dict[str, CommandModel.Command]:
        dictionary = {}
        for command in self.listOfCommands:
            dictionary[command.GetCommandName()] = command
        return dictionary

class DefaultCommand(CommandModel.Command):
    def __init__(self):
        self.data = []
        super().__init__("test")

    def RunThisCommand(self, data : dict = {}) -> str:
        print("Hello World!")
        pass