descriptions = {
        "chatEffect" : "If there is an chat effect applied, setting this to False will block the chat effect from applying.\nIf you have a chat effect that runs a command, disable this on the effect to avoid feedback loops.",
        "feedback" : "With this set to false, the command will not give feedback to the user.\nThis is useful for commands that are used to set up other commands, or if you just don't want to get feedback."   
            }

lessImportantCommands = {
    "cmd": {
        "description": "Launches commandprompt.",
        "function": """\ncommand = "{}"\nkeep = {}\nimport os\nif keep == True:\n    msg = "cmd /k "\nelse:\n    msg = ""\nif command == "":\n    os.system("cmd")\nelse: \n    os.system(msg + command)\n""",
        "parameters": {
            "var1": {
                "default": "",
                "given": "-cmd",
                "description": "An command to run in the commandprompt."
            },
            "var2": {
                "default": "False",
                "given": "-k",
                "description": "Keep cmd open after command is done. (might break multi-line commands)",
                "options": ["True", "False"]
            }
        },
        "category": ["default", "tool", "less important"]
    },
    "playSound" : {
        "description": "Play a sound.",
        "function": """sound = \"{}\";path = \"{}\";ignore = {};
if ignore == True:
    try:
        from playsound import playsound;playsound(path + sound);
    except:
        pass;
else:
    from playsound import playsound;playsound(path + sound);""",
        "parameters" : {
            "var1": {
                "default": "newSup.mp3",
                "given": "-sound",
                "description": "The sound file."
            },
            "var2": {
                "default": "data/audio/",
                "given": "-path",
                "description": "The path to the sound file."
            },
            "var3": {
                "default": "False",
                "given": "-ignoreError",
                "description": "If True, the error will be ignored.",
                "options": ["True", "False"]
            }
        },
        "category": ["default", "less important", "effect"]
    },
    "wait" : {
        "description": "Wait for a certain amount of seconds.",
        "function": "seconds = {};import time;time.sleep(seconds);",
        "parameters" : {
            "var1": {
                "default": "1",
                "given": "-seconds",
                "description": "The amount of seconds to wait."
            }
        },
        "category": ["default", "effect", "less important"]
    },
    "clearConsole" : {
        "description": "Clears the console.",
        "function": "import os;os.system('cls');",
        "parameters" : {},
        "category": ["default", "tool", "effect", "less important"]
    },
    "getMetaData": {
        "description": "Get the metadata of anything.",
        "function": "textHandler.textController(defaultCommands.formatMetaData(defaultCommands.getMetaData(\"{}\", \"{}\")), chatEffect = {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "help",
                "given": "-name",
                "description": "The variable to get the metadata of.",
                "options": ["help", "list"]
            },
            "var2" : {
                "default": "command",
                "given": "-type",
                "description": "The type of thing you want metadata of.",
                "options": ["command", "preset", "library", "program"]
            },
            "var3": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "tool", "less important"]
    },
}

defaultPresetCommands = {
    "preset" : {
        "description": "Set name of preset, or more with parameters.",
        "function": """name = \"{}\";save = {};load = \"{}\";chatEffect1 = {}; feedback = {}
if name == \"\" and save == False and load == \"\": 
    textHandler.textController(\"Preset Loaded: \" + str(preset.getPreset()), chatEffect = chatEffect1, feedback = feedback);); 
if name != \"\": 
    preset.setName(name, chatEffect = chatEffect1, feedback = feedback); 
if save == True: 
    preset.savePreset(chatEffect = chatEffect1, feedback = feedback); 
if load != \"\": 
    preset.loadPreset(load, chatEffect = chatEffect1, feedback = feedback)""",
        "parameters": {
            "var1": {
                "default": "",
                "given": "-name",
                "description": "Set the name of the preset."
            },
            "var2": {
                "default": "False",
                "given": "-save",
                "description": "Save the current preset.",
                "options": ["True", "False"]
            },
            "var3": {
                "default": "",
                "given": "-load",
                "description": "Load a preset."
            },
            "var4": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var5": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "preset"]
    }
}

defaultCommands = {
    "exit": {
        "description": "Exits the program.",
        "function": "try:\n    activeThreadStopper.stopped = True\nexcept:\n    exit()",
        "parameters": {},
        "category": ["default"],
        "metaData": {
            "name" : "Exit command",
            "description" : "The built in exit command of the virtualBBQduck program.",
            "version" : "2.1.0",
            "author" : "OldMartijntje"
        },
        "useSpecialParameters": True
    },
    "print": {
        "description": "Prints the given text.",
        "function": "print(\"{}\")",
        "parameters": {
            "var1": {
                "default": "Hello World!",
                "given": "-txt",
                "description": "The text to print."
            }
        },
        "category": ["default"]
    },
    "help": {
        "description": "Displays help of any command, or itself if no command is given.\nUse '-params True' to display the parameters of the command.",
        "function": "textHandler.textController(defaultCommands.getInfoFromCommand(\"{}\", {}, {}, {}), chatEffect = {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "help",
                "given": "-cmd",
                "description": "The command to display help for."
            },
            "var2": {
                "default": "True",
                "given": "-params",
                "description": "Give the parameters of the command.",
                "options": ["True", "False"]
            },
            "var3": {
                "default": "False",
                "given": "-category",
                "description": "Show the category of the command.",
                "options": ["True", "False"]
            },
            "var3.1": {
                "default": "False",
                "given": "-defaultParams",
                "description": "Show the default parameters per parameter.",
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var5": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "help"],
        "metaData": {
            "name" : "Help command",
            "description" : "The built in help command of the virtualBBQduck program.",
            "version" : "1.0.0",
            "author" : "OldMartijntje"
        }
    },
    "list": {
        "description": "Lists all commands and/or categories.",
        "function": "textHandler.textController(defaultCommands.listCommands(\"{}\", {}), chatEffect = {}, feedback = {})",
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
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "help"],
        "metaData": {
            "name" : "list command",
            "description" : "The built in list command of the virtualBBQduck program.",
            "version" : "1.0.0",
            "author" : "OldMartijntje"
        }
    },
    "listCategories": {
        "description": "Lists all categories.",
        "function": "textHandler.textController(defaultCommands.listCategories(), chatEffect = {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var2": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
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
        "function": "file = open(\"{}/{}\", \"r\");textHandler.textController(file.read(), chatEffect = {}, feedback = {});file.close()",
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
            },
            "var3": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
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
        "function": "command=\"{}\";textHandler.textController((defaultCommands.getCommandData(command) if defaultCommands.getCommandData(command) != False else \"Command not found\"), chatEffect = {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "help",
                "given": "-cmd",
                "description": "The command to print."
            },
            "var2": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var3": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "coding", "debug"]
    },
    "loadDefaultCommands": {
        "description": "Loads the default commands.",
        "function": "defaultCommands.loadDefaultCommands({}, {}, {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "False",
                "given": "-force",
                "description": "Force the default commands to load, this means no confirmation will be asked.",
                "options": ["True", "False"]
            },
            "var2": {
                "default": "False",
                "given": "-overwrite",
                "description": "If True, the default commands will overwrite the current commands in DefaultData.json and then load them.\nThis is a reset command, it will reset the default commands to the default commands hardcoded.",
                "options": ["True", "False"]
            },
            "var3": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "debug"],
        "metaData": {
            "name" : "LoadDefaultCommands command",
            "description" : "The built in LoadDefaultCommands command of the virtualBBQduck program.",
            "version" : "1.0.0",
            "author" : "OldMartijntje"
        }
    },
}

failsafeCommands = {
    "loadDefaultCommands": {
        "description": "Loads the default commands.",
        "function": "defaultCommands.loadDefaultCommands({}, {}, {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "False",
                "given": "-force",
                "description": "Force the default commands to load, this means no confirmation will be asked.",
                "options": ["True", "False"]
            },
            "var2": {
                "default": "False",
                "given": "-overwrite",
                "description": "If True, the default commands will overwrite the current commands in DefaultData.json and then load them.\nThis is a reset command, it will reset the default commands to the default commands hardcoded.",
                "options": ["True", "False"]
            },
            "var3": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var4": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "debug", "failsafe"],
        "metaData": {
            "name" : "LoadDefaultCommands command",
            "description" : "The built in Failsafe LoadDefaultCommands command of the virtualBBQduck program.",
            "version" : "1.0.0",
            "author" : "OldMartijntje"
        }
    },
    "help" : {
        "description": "Prints the help menu.",
        "function": "textHandler.textController(\"The original \\\"help\\\" command is deleted somehow, run 'loadDefaultCommands -force True -overwrite True' to reset the default commands.\", chatEffect = {}, feedback = {})",
        "parameters": {
            "var1": {
                "default": "True",
                "given": "-chatEffect",
                "description": descriptions["chatEffect"],
                "options": ["True", "False"]
            },
            "var2": {
                "default": "True",
                "given": "-feedback",
                "description": descriptions["feedback"],
                "options": ["True", "False"]
            }
        },
        "category": ["default", "help", "failsafe"],
        "metaData": {
            "name" : "Help command",
            "description" : "The built in Failsafe help command of the virtualBBQduck program.",
            "version" : "1.0.0",
            "author" : "OldMartijntje"
        }
    }
}