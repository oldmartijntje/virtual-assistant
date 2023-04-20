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
    preset.currentPreset.data["loop"] = 0
import atexit

def exit_handler():
    for item in setup.readJson("configuration/settings.json")["exit"]["exitCommands"]:
        inputHandler.givenInput(item)
        preset.currentPreset.data["loop"] = 0
    if preset.currentPreset.data["settings"]["autoSave"] == True:
        preset.savePreset()
    if setup.readJson("configuration/settings.json")["exit"]["presetsCanHaveCustomExitCommands"]:
        for item in preset.currentPreset.data["exitCommands"]:
            inputHandler.givenInput(item)
            preset.currentPreset.data["loop"] = 0
    logger.info('Exit complete')

atexit.register(exit_handler)

import threading
import time

def wait_for_input():
    while True:
        inputHandler.givenInput(input())
        preset.currentPreset.data["loop"] = 0

def handle_scheduled_tasks():
    while True:
        # perform scheduled tasks and stuff
        settings = setup.readJson("configuration/settings.json")
        if settings["async"]["enableCommands"]:
            for item in setup.readJson("configuration/settings.json")["async"]["perLoopCommands"]:
                inputHandler.givenInput(item)
                preset.currentPreset.data["loop"] = 0
        time.sleep(settings["async"]["loopTime"])

input_thread = threading.Thread(target=wait_for_input)
if setup.readJson("configuration/settings.json")["async"]["enable"]:
    task_thread = threading.Thread(target=handle_scheduled_tasks)

input_thread.start()
task_thread.start()

input_thread.join()
task_thread.join()