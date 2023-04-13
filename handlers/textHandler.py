import handlers.inputHandler as inputHandler
def textController(text, settings = {}, chatEffect = True, feedback=True):
    from shared.logger import logger
    import setup as setup
    import model.preset as preset
    logger.debug('textController called')
    if (settings == {}):
        try:
            settings = setup.readJson("configuration/settings.json")
        except Exception as e:
            logger.error(f'in the textController: {e}')
            settings = setup.defaultSettings
    if feedback == True:

        presetData = preset.getPresetData()

        if chatEffect == True:
            if "settings" in presetData and "activeEffects" in presetData["settings"]:
                for effect in presetData["settings"]["activeEffects"]: 
                    if effect in presetData["effects"] and "commands" in presetData["effects"][effect] and "beforeText" in presetData["effects"][effect]["commands"]:
                        for item in presetData["effects"][effect]["commands"]["beforeText"]:
                            inputHandler.givenInput(item)

                    if effect in presetData["effects"] and "text" in presetData["effects"][effect]:
                        if "beforeText" in presetData["effects"][effect]["text"]:
                            text = presetData["effects"][effect]["text"]["beforeText"] + text
                        if "afterText" in presetData["effects"][effect]["text"]:
                            text = text + presetData["effects"][effect]["text"]["afterText"]
                    
                    if effect in presetData["effects"] and "replaceText" in presetData["effects"][effect]:
                        for item in list(presetData["effects"][effect]["replaceText"].keys()):
                            text = text.replace(item, presetData["effects"][effect]["replaceText"][item])

        if (settings["textSettings"]["printFormat"]["enabled"] == True):
            newText = settings["textSettings"]["printFormat"]["defaultFormatting"]["start"] + str(text) + settings["textSettings"]["printFormat"]["defaultFormatting"]["end"]
            print(newText)
        else:
            print(text)

        if chatEffect == True:
            if "settings" in presetData and "activeEffects" in presetData["settings"]:
                for effect in presetData["settings"]["activeEffects"]: 
                    if effect in presetData["effects"] and "commands" in presetData["effects"][effect] and "afterText" in presetData["effects"][effect]["commands"]:
                        for item in presetData["effects"][effect]["commands"]["afterText"]:
                            inputHandler.givenInput(item)
    else:
        logger.debug('no feedback asked')