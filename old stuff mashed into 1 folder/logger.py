# app_logger.py
import logging
import setup as setup
import datetime
settings = setup.readJson("configuration/settings.json")

# Define a module-level logger object
logger = logging.getLogger(settings["logging"]["appName"])
match settings["logging"]["consoleLevel"]:  
    case "DEBUG":
        logger.setLevel(logging.DEBUG)
    case "INFO":
        logger.setLevel(logging.INFO)
    case "WARNING":
        logger.setLevel(logging.WARNING)
    case "ERROR":
        logger.setLevel(logging.ERROR)
    case "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    case _:   
        logger.setLevel(logging.WARNING)

# Create a console handler
ch = logging.StreamHandler()
match settings["logging"]["consoleLevel"]:  
    case "DEBUG":
        ch.setLevel(logging.DEBUG)
    case "INFO":
        ch.setLevel(logging.INFO)
    case "WARNING":
        ch.setLevel(logging.WARNING)
    case "ERROR":
        ch.setLevel(logging.ERROR)
    case "CRITICAL":
        ch.setLevel(logging.CRITICAL)
    case _:   
        ch.setLevel(logging.WARNING)

# Create a file handler
filename = datetime.datetime.now().strftime(settings["logging"]["filenameWithDatetimeFormatting"]) + '.log'
folder = settings["logging"]["folder"]

fh = logging.FileHandler(f'{folder}/{filename}')
fh.setLevel(logging.INFO)
match settings["logging"]["fileLevel"]:  
    case "DEBUG":
        fh.setLevel(logging.DEBUG)
    case "INFO":
        fh.setLevel(logging.INFO)
    case "WARNING":
        fh.setLevel(logging.WARNING)
    case "ERROR":
        fh.setLevel(logging.ERROR)
    case "CRITICAL":
        fh.setLevel(logging.CRITICAL)
    case _:   
        fh.setLevel(logging.WARNING)

# Create a formatter
formatter = logging.Formatter(settings["logging"]["format"])

# Add the formatter to the handlers
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(ch)
logger.addHandler(fh)