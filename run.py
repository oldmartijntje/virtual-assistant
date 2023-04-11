import shared.setup as setup
import shared.feedback.textHandling as textHandling
if (setup.createJsonIfNotExists("configuration/settings.json")): 
    textHandling.textController("Created settings.json")

textHandling.textController(setup.readJson("configuration/settings.json"), setup.readJson("configuration/settings.json"))
input()