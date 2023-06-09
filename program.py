import models.AssistantModel as AssistantModel
import models.ContextModel as ContextModel
import models.CommandHandlerModel as CommandHandlerModel

context = ContextModel.Context()
commandHandler = CommandHandlerModel.CommandHandler()
assistant = AssistantModel.Assistant(context, commandHandler)