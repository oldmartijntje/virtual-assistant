def givenInput(input):
    import handlers.textHandling as textHandling
    from shared.logger import logger
    logger.debug(f'givenInput called: {input}')
    if (input == "exit"):
        exit()
    else:
        textHandling.textController("Invalid input")
        return False