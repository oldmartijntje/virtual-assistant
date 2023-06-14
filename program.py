import models.AssistantModel as AssistantModel
import models.ContextModel as ContextModel
import models.CommandHandlerModel as CommandHandlerModel
import libraries.DefaultLibrary as DefaultLibrary

# context = ContextModel.Context()
# commandHandler = CommandHandlerModel.CommandHandler()
# assistant = AssistantModel.Assistant(context, commandHandler)

lib = DefaultLibrary.DefaultLibrary()
lib.listOfCommands[0].RunThisCommand()
handler = CommandHandlerModel.CommandHandler()
handler.AddLibrary(lib)
handler.commandDict["test"].RunThisCommand()
context = ContextModel.Context()
assistance = AssistantModel.Assistant(context, handler)