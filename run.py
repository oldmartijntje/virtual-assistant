import shared.setup as setup
import handlers.textHandling as textHandling
import handlers.inputHandler as inputHandler
from shared.logger import logger
import model.preset as preset
preset.currentPreset.data["loop"] = 0
logger.debug('logger inported')
logger.info('Startup complete')
for item in setup.readJson("configuration/settings.json")["startup"]["startupCommands"]:
    inputHandler.givenInput(item)
while True:
    inputHandler.givenInput(input())
    preset.currentPreset.data["loop"] = 0