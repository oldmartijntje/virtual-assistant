def textController(text, settings = {}):
    from shared.logger import logger
    logger.debug('textController called')
    if (settings != {} and settings["textSettings"]["printFormat"]["enabled"] == True):
        newText = settings["textSettings"]["printFormat"]["defaultFormatting"]["start"] + str(text) + settings["textSettings"]["printFormat"]["defaultFormatting"]["end"]
        print(newText)
    else:
        print(text)