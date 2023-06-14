import models.ContextModel as ContextModel
import models.LibraryModel as LibraryModel

class CommandHandler:
    def __init__(self):
        self.commandDict = {}

    def ExecuteCommand(self, command: dict, context: ContextModel.Context) -> None:
        pass

    def TranslateFromContext(self, string: dict, context: ContextModel.Context) -> str:
        pass

    def AddLibraries(self) -> list:
        pass

    def SplitCommand(self, command: list) -> list[str]:
        pass

    def AddLibrary(self, lib: LibraryModel.Library) -> None:
        """
    Imports a Library and returns True or False
    """
        self.commandDict.update(lib.GetCommands())