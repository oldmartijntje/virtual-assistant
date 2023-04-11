import shared.setup as setup
import handlers.textHandling as textHandling
import handlers.inputHandler as inputHandler
from shared.logger import logger
logger.debug('logger inported')
logger.info('Startup complete')
for item in setup.readJson("configuration/settings.json")["startup"]["startupCommands"]:
    inputHandler.givenInput(item)
while True:
    inputHandler.givenInput(input())