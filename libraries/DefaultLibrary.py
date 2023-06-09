import models.LibraryModel as LibraryModel
import models.CommandModel as CommandModel

class DefaultLibrary(LibraryModel.Library):
    def __init__(self):
        self.listOfCommands = []
        self.listOfCommands.append(DefaultCommand())

    def GetCommands() -> list[CommandModel.Command]:
        pass

class DefaultCommand(CommandModel.Command):
    def __init__(self):
        self.data = []

    def RunThisCommand(command : dict) -> str:
        print("Hello World!")
        pass