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

defaultData ={
    "defaultCommands": {
        "exit": {
            "description": "Exits the program",
            "function": "exit()",
            "parameters": {},
            "category": ["default"]
        },
        "print": {
            "description": "Prints the given text",
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
                    "description": "The command to display help for"
                },
                "var2": {
                    "default": "False",
                    "given": "-params",
                    "description": "Give the parameters of the command"
                },
                "var3": {
                    "default": "False",
                    "given": "-category",
                    "description": "Show the category of the command"
                }
            },
            "category": ["default", "help"]
        },
        "list": {
            "description": "Lists all commands",
            "function": "textHandling.textController(defaultCommands.listCommands(\"{}\", {}))",
            "parameters": {
                "var1": {
                    "default": "",
                    "given": "-category",
                    "description": "The category to list"
                },
                "var2": {
                    "default": "40",
                    "given": "-amount",
                    "description": "the amount of characters to display per item"
                }
            },
            "category": ["default", "help"]
        },
        "mkfile": {
            "description": "Creates a file",
            "function": """file = open(\"{}/{}.{}\", \"a\");file.write("{}");file.close()""",
            "parameters": {
                "var1": {
                    "default": "configuration",
                    "given": "-path",
                    "description": "The path to the file"
                },
                "var2": {
                    "default": "test",
                    "given": "-name",
                    "description": "The name of the file"
                },
                "var3": {
                    "default": "txt",
                    "given": "-extension",
                    "description": "The extension of the file"
                },
                "var4": {
                    "default": "Hello World!",
                    "given": "-content",
                    "description": "The content of the file"
                }
            },
            "category": ["default", "file"]
        },
        "mkfolder": {
            "description": "Creates a folder",
            "function": "os.makedirs(\"{}\")",
            "parameters": {
                "var1": {
                    "default": "configuration",
                    "given": "-path",
                    "description": "The path to the folder"
                }
            }, 
            "category": ["default", "file"]
        },
        "delFile": {
            "description": "Deletes a file",
            "function": "os.remove(\"{}/{}\")",
            "parameters": {
                "var1": {
                    "default": "configuration",
                    "given": "-path",
                    "description": "The path to the file"
                },
                "var2": {
                    "default": "test.txt",
                    "given": "-file",
                    "description": "The file to delete"
                }
            },
            "category": ["default", "file"]
        },
    }
}

def createJsonIfNotExists(path, data = defaultSettings):
    import os, json
    if not os.path.exists(path):
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
createJsonIfNotExists("configuration/defaultData.json", defaultData)