import models.ContextModel as ContextModel
import models.CommandHandlerModel as CommandHandlerModel

class Assistant:
    def __init__(self, context : ContextModel.Context, commandHandler : CommandHandlerModel.CommandHandler):
        self.programSettings = {}
        self.commandHandler = commandHandler
        self.context = context

    def ExecuteCommand(self, command: str) -> None:
        splittedCommand = self.commandHandler.SplitCommand(command)
        splittedCommand = self.commandHandler.TranslateFromContext(splittedCommand, self.context)
        commandDict = self.commandHandler.CommandToDict(splittedCommand)
        self.ExecuteCommandByDict(commandDict)

    def ExecuteCommandByDict(self, command: dict) -> None:
        print(command)
    