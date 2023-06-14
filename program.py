import models.AssistantModel as AssistantModel
import models.ContextModel as ContextModel
import models.CommandHandlerModel as CommandHandlerModel
import libraries.DefaultLibrary as DefaultLibrary

# context = ContextModel.Context()
# commandHandler = CommandHandlerModel.CommandHandler()
# assistant = AssistantModel.Assistant(context, commandHandler)

lib = DefaultLibrary.DefaultLibrary()
handler = CommandHandlerModel.CommandHandler()
handler.AddLibrary(lib)
context = ContextModel.Context()
assistance = AssistantModel.Assistant(context, handler)
assistance.ExecuteCommand("test 2 nice 'henk de steen'")
assistance.ExecuteCommandByDict({"command" : "test", "arguments": [2, "nice", "henk de steen"]})