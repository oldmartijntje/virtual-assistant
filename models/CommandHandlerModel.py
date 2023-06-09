import models.ContextModel as ContextModel
class CommandHandler:
    def __init__(self):
        self.commandList = []

    def ExecuteCommand(command: dict, context: ContextModel.Context) -> None:
        pass

    def TranslateFromContext(string: dict, context: ContextModel.Context) -> str:
        pass

    def AddLibraries() -> list:
        pass

    def SplitCommand(command: list) -> list[str]:
        pass