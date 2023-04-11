def textController(text, settings = {}):
    from shared.logger import logger
    import shared.setup as setup
    logger.debug('textController called')
    if (settings == {}):
        try:
            settings = setup.readJson("configuration/settings.json")
        except Exception as e:
            logger.error(e)
            settings = setup.defaultSettings
    if (settings["textSettings"]["printFormat"]["enabled"] == True):
        newText = settings["textSettings"]["printFormat"]["defaultFormatting"]["start"] + str(text) + settings["textSettings"]["printFormat"]["defaultFormatting"]["end"]
        print(newText)
    else:
        print(text)