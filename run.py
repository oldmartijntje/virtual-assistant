import shared.setup as setup
import handlers.textHandling as textHandling
import handlers.inputHandler as inputHandler
from shared.logger import logger
import model.preset as preset
logger.debug('logger inported')
logger.info('Startup complete')
# for item in setup.readJson("configuration/settings.json")["startup"]["startupCommands"]:
#     inputHandler.givenInput(item)
preset.currentPreset.data["loop"] = 0
while True:
    inputHandler.givenInput(input())
    preset.currentPreset.data["loop"] = 0