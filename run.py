import shared.setup as setup
import shared.feedback.textHandling as textHandling
if (setup.createJsonIfNotExists("configuration/settings.json")): 
    textHandling.textController("Created settings.json")
from shared.logger import logger
logger.debug('Debug message')
textHandling.textController(setup.readJson("configuration/settings.json"), settings = setup.readJson("configuration/settings.json"))
input()