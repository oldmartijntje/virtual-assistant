import models.ContextModel as ContextModel
import models.CommandHandlerModel as CommandHandlerModel

class Assistant:
    def __init__(self, context : ContextModel.Context, commandHandler : CommandHandlerModel.CommandHandler):
        self.programSettings = {}
        self.commandHandler = commandHandler
        self.context = context

    def ExecuteCommand(command: str) -> None:
        pass

    def ExecuteCommandByDict(command: dict) -> None:
        pass
    