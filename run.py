import shared.setup as setup
import handlers.textHandling as textHandling
import handlers.inputHandler as inputHandler
if (setup.createJsonIfNotExists("configuration/settings.json")): 
    textHandling.textController("Created settings.json")
from shared.logger import logger
logger.debug('logger inported')
logger.info('Startup complete')
while True:
    inputHandler.givenInput(input())