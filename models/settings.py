import copy

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
        },
        "maximumRecursion": 10
    },
    "logging": {
        "enabled": True,
        "defaultLevel": "INFO",
        "consoleLevel": "WARNING",
        "fileLevel": "INFO",
        "folder": "logs",
        "filename": "default.log",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "filenameWithDatetimeFormatting": "VBBQD%Y-%m-%d_%H",
        "appName" : "virtualBBQduck"
    },
    "startup": {
        "startupCommands": [
            "print -txt \"Welcome to the virtual BBQ duck!\\n\\nType any command to begin\\nIf you find yourself stuck, 'help', 'list' and 'listCategories' might help you!\""
            ]
    },
    "exit": {
        "exitCommands": [
            "print -txt Goodbye!"
        ],
        "presetsCanHaveCustomExitCommands": False
    },
    "async": {
        "enabled": True,
        "commands": {
            "perLoopCommands": [
                "print -txt 'testing async!'"
            ],
            "enabled": False,
            "loopTime": 1,
            # "loopTime": 1 = 1 second
        },
        "network": {
            "enabled": False,   
            "client": {
                "enabled": False,
                "host": "127.0.0.1",
                "port": 1234,
                "username": "default",
                "retries": 20
            },
            "server": {
                "enabled": False,
                "port": 1234,
                "username": "default"
            }
        }
    },
    "flaggedWords": [
        "flaggedWordExample"
    ],
    "password": "",
    "preferences": {
        "username": "",
        "anonymous": False,
    }
}

debugDefaultSettings = copy.deepcopy(defaultSettings)
debugDefaultSettings["logging"]["defaultLevel"] = "DEBUG"
debugDefaultSettings["logging"]["consoleLevel"] = "DEBUG"
debugDefaultSettings["logging"]["fileLevel"] = "INFO"
debugDefaultSettings["password"] = "20" # 20 decoded is a space