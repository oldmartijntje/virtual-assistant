import setup as setup
import handlers.textHandler as textHandler
import handlers.inputHandler as inputHandler
from shared.logger import logger
import models.preset as preset
preset.currentPreset.data["loop"] = 0
logger.debug('logger inported')
logger.info('Startup complete')
for item in setup.readJson("configuration/settings.json")["startup"]["startupCommands"]:
    inputHandler.givenInput(item)
import atexit

def exit_handler():
    for item in setup.readJson("configuration/settings.json")["exit"]["exitCommands"]:
        inputHandler.givenInput(item)
    if preset.currentPreset.data["settings"]["autoSave"] == True:
        preset.savePreset()
    if setup.readJson("configuration/settings.json")["exit"]["presetsCanHaveCustomExitCommands"]:
        for item in preset.currentPreset.data["exitCommands"]:
            inputHandler.givenInput(item)
    logger.info('Exit complete')

atexit.register(exit_handler)

while True:
    inputHandler.givenInput(input())
    preset.currentPreset.data["loop"] = 0
