import setup as setup
import handlers.textHandler as textHandler
import handlers.clientConnectionHandler as clientConnectionHandler
import handlers.serverHostHandler as serverHostHandler
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
import models.threadStopper as threadStopper
activeThreadStopper = threadStopper.Stopper()

def exit_handler():
    global data
    for item in setup.readJson("configuration/settings.json")["exit"]["exitCommands"]:
        inputHandler.givenInput(item)
        preset.currentPreset.data["loop"] = 0
    if preset.currentPreset.data["settings"]["autoSave"] == True:
        preset.savePreset()
    logger.info('Going to overwrite Data')
    setup.createJsonIfNotExists("data/json/personalData.json", data, True)
    logger.info('Data overwritten')
    if setup.readJson("configuration/settings.json")["exit"]["presetsCanHaveCustomExitCommands"]:
        for item in preset.currentPreset.data["exitCommands"]:
            inputHandler.givenInput(item)
            preset.currentPreset.data["loop"] = 0
    logger.info('Exit complete')

atexit.register(exit_handler)

import threading
import time

def wait_for_input():
    global activeThreadStopper
    while not activeThreadStopper.stopped:
        inputHandler.givenInput(input(), activeThreadStopper)
        preset.currentPreset.data["loop"] = 0

def handle_scheduled_tasks():
    while not activeThreadStopper.stopped:
        # perform scheduled tasks and stuff
        settings = setup.readJson("configuration/settings.json")
        if settings["async"]["commands"]["enabled"]:
            for item in setup.readJson("configuration/settings.json")["async"]["commands"]["perLoopCommands"]:
                inputHandler.givenInput(item, data)
                preset.currentPreset.data["loop"] = 0
        time.sleep(settings["async"]["commands"]["loopTime"])

data = setup.readJson("data/json/personalData.json")
input_thread = threading.Thread(target=wait_for_input)
input_thread.start()
if setup.readJson("configuration/settings.json")["async"]["enabled"]:
    task_thread = threading.Thread(target=handle_scheduled_tasks)
    task_thread.start()
    if setup.readJson("configuration/settings.json")["async"]["network"]["enabled"]:
        if setup.readJson("configuration/settings.json")["async"]["network"]["client"]["enabled"]:
            client_thread = threading.Thread(target=clientConnectionHandler.start_client_connection_handler, args=(activeThreadStopper,))
            client_thread.start()
        if setup.readJson("configuration/settings.json")["async"]["network"]["server"]["enabled"]:
            server_thread = threading.Thread(target=serverHostHandler.start_server_host_handler, args=(activeThreadStopper,))
            server_thread.start()
            

input_thread.join()
if setup.readJson("configuration/settings.json")["async"]["enabled"]:
    task_thread.join()
    if setup.readJson("configuration/settings.json")["async"]["network"]["enabled"]:
        if setup.readJson("configuration/settings.json")["async"]["network"]["client"]["enabled"]:
            client_thread.join()
        if setup.readJson("configuration/settings.json")["async"]["network"]["server"]["enabled"]:
            server_thread.join()


