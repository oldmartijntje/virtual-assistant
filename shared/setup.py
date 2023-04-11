defaultSettings = {
    "textSettings": {
        "textToSpeach": {
            "enabled": True,
        },
        "printFormat" : {
            "enabled": True,
            "defaultFormatting": {
                "start": "\033[4;3;1m",
                "end": "\033[0m"
            }
        }
    },
    "logging": {
        "enabled": True,
        "defaultLevel": "DEBUG",
        "consoleLevel": "DEBUG",
        "fileLevel": "DEBUG",
        "folder": "logs",
        "filename": "default.log",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "filenameWithDatetimeFormatting": "VBBQD%Y-%m-%d_%H",
        "appName" : "virtualBBQduck"
    }
}

defaultPresetHandler = {
    "presetNames": {
        
    }
}

defaultCommands ={
    "exit": {
        "description": "Exits the program.",
        "function": "exit()",
        "parameters": {},
        "category": ["default"]
    },
    "print": {
        "description": "Prints the given text.",
        "function": "print(\"{}\")",
        "parameters": {
            "var1": {
                "default": "Hello World!",
                "given": "-txt"
            }
        },
        "category": ["default"]
    },
    "help": {
        "description": "Displays help of any command, or itself if no command is given.\nUse '-params True' to display the parameters of the command.",
        "function": "textHandling.textController(defaultCommands.getInfoFromCommand(\"{}\", {}, {}))",
        "parameters": {
            "var1": {
                "default": "help",
                "given": "-cmd",
                "description": "The command to display help for."
            },
            "var2": {
                "default": "False",
                "given": "-params",
                "description": "Give the parameters of the command."
            },
            "var3": {
                "default": "False",
                "given": "-category",
                "description": "Show the category of the command."
            }
        },
        "category": ["default", "help"]
    },
    "list": {
        "description": "Lists all commands and/or categories.",
        "function": "textHandling.textController(defaultCommands.listCommands(\"{}\", {}, {}))",
        "parameters": {
            "var1": {
                "default": "",
                "given": "-fCategory",
                "description": "Filter on a category to list."
            },
            "var2": {
                "default": "40",
                "given": "-amount",
                "description": "the amount of characters to display per item."
            },
            "var3": {
                "default": "False",
                "given": "-lCategories",
                "description": "List all categories."
            }
        },
        "category": ["default", "help"]
    },
    "mkfile": {
        "description": "Creates a file.",
        "function": """file = open(\"{}/{}.{}\", \"a\");file.write("{}");file.close()""",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the file."
            },
            "var2": {
                "default": "test",
                "given": "-name",
                "description": "The name of the file."
            },
            "var3": {
                "default": "txt",
                "given": "-extension",
                "description": "The extension of the file."
            },
            "var4": {
                "default": "Hello World!",
                "given": "-content",
                "description": "The content of the file."
            }
        },
        "category": ["default", "file"]
    },
    "mkfolder": {
        "description": "Creates a folder.",
        "function": "os.makedirs(\"{}\")",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the folder."
            }
        }, 
        "category": ["default", "file"]
    },
    "rmFile": {
        "description": "Deletes a file.",
        "function": "os.remove(\"{}/{}\")",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the file."
            },
            "var2": {
                "default": "test.txt",
                "given": "-file",
                "description": "The file to delete."
            }
        },
        "category": ["default", "file"]
    },
    "delFolder": {
        "description": "Deletes a folder.",
        "function": "os.rmdir(\"{}\")",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the folder."
            }
        },
        "category": ["default", "file"]
    },
    "readFile": {
        "description": "Reads a file.",
        "function": "file = open(\"{}/{}\", \"r\");textHandling.textController(file.read());file.close()",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the file."
            },
            "var2": {
                "default": "test.txt",
                "given": "-file",
                "description": "The file to read."
            }
        },
        "category": ["default", "file"]
    },
    "writeFile": {
        "description": "Writes to a file.",
        "function": "file = open(\"{}/{}\", \"w\");file.write(\"{}\");file.close()",
        "parameters": {
            "var1": {
                "default": "configuration",
                "given": "-path",
                "description": "The path to the file."
            },
            "var2": {
                "default": "test.txt",
                "given": "-file",
                "description": "The file to write to."
            },
            "var3": {
                "default": "Hello World!",
                "given": "-content",
                "description": "The content to write to the file."
            }
        },
        "category": ["default", "file"]
    },
    "cmdPrint" : { 
        "description": "Prints command from a command.",
        "function": "command=\"{}\";textHandling.textController(defaultCommands.getCommandData(command) if defaultCommands.getCommandData(command) != False else \"Command not found\")",
        "parameters": {
            "var1": {
                "default": "help",
                "given": "-cmd",
                "description": "The command to print."
            }
        },
        "category": ["default", "coding", "debug"]
    },
    "loadDefaultCommands": {
        "description": "Loads the default commands.",
        "function": "defaultCommands.loadDefaultCommands({}, {})",
        "parameters": {
            "var1": {
                "default": "False",
                "given": "-force",
                "description": "Force the default commands to load, this means no confirmation will be asked."
            },
            "var2": {
                "default": "False",
                "given": "-overwrite",
                "description": "If True, the default commands will overwrite the current commands in DefaultData.json and then load them.\nThis is a reset command, it will reset the default commands to the default commands hardcoded."
            }
        },
        "category": ["default", "debug"]
    },
}

failsafeCommands = {
    "loadDefaultCommands": {
        "description": "Loads the default commands.",
        "function": "defaultCommands.loadDefaultCommands({}, {})",
        "parameters": {
            "var1": {
                "default": "False",
                "given": "-force",
                "description": "Force the default commands to load, this means no confirmation will be asked."
            },
            "var2": {
                "default": "False",
                "given": "-overwrite",
                "description": "If True, the default commands will overwrite the current commands in DefaultData.json and then load them.\nThis is a reset command, it will reset the default commands to the default commands hardcoded."
            }
        },
        "category": ["default", "debug", "failsafe"]
    },
    "help" : {
        "description": "Prints the help menu.",
        "function": "textHandling.textController(\"The original \\\"help\\\" command is deleted somehow, run 'loadDefaultCommands -force True -overwrite True' to reset the default commands.\")",
        "category": ["default", "help", "failsafe"]
    }
}

defaultPresetCommands = {
    "preset" : {
        "description": "Set name of preset, or more with parameters.",
        "function": """name = \"{}\";save = {};load = \"{}\";
if name == \"\" and save == False and load == \"\": 
    textHandling.textController(\"Preset Loaded: \" + str(preset.getPreset())); 
if name != \"\": 
    preset.setName(name); 
if save == True: 
    preset.savePreset(); 
if load != \"\": 
    preset.loadPreset(load)""",
        "parameters": {
            "var1": {
                "default": "",
                "given": "-name",
                "description": "Set the name of the preset."
            },
            "var2": {
                "default": "False",
                "given": "-save",
                "description": "Save the current preset."
            },
            "var3": {
                "default": "",
                "given": "-load",
                "description": "Load a preset."
            }
        },
        "category": ["default", "preset"]
    }
}

lessImportantCommands = {
    "cmd": {
        "description": "Launches commandprompt.",
        "function": """command = \"{}\";import os;
if command == \"\":
    os.system(\"cmd\");
else: 
    os.system(\"cmd /c \" + command)""",
        "parameters": {
            "var1": {
                "default": "",
                "given": "-cmd",
                "description": "An command to run in the commandprompt."
            }
        },
        "category": ["default", "tool", "less important"]
    },
}


defaultCommands.update(defaultPresetCommands)
defaultCommands.update(lessImportantCommands)

def createJsonIfNotExists(path, data = defaultSettings, overwrite = False):
    import os, json
    if not os.path.exists(path) or overwrite == True:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return True
    else:
        return False
    
def readJson(path):
    import json
    with open(path, "r") as f:
        return json.load(f)
    
def create_directory(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)

createJsonIfNotExists("configuration/settings.json")
settings = readJson("configuration/settings.json")
if (settings["logging"]["enabled"] == True):
        create_directory(settings["logging"]["folder"])
create_directory("configuration")
create_directory("configuration/presetData")
createJsonIfNotExists("configuration/presetData/presetHandler.json", defaultPresetHandler)
createJsonIfNotExists("configuration/defaultFunctions.json", defaultCommands)