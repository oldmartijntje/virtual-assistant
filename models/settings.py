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
            "playSound -ignoreError True",
            "clearConsole",
            "print -txt \"Welcome to the virtual BBQ duck!\\n\\nType any command to begin\\nIf you find yourself stuck, 'help' and 'list' might help you!\"",
            "playSound"
            ]
    },
    "flaggedWords": [
        "flaggedWordExample"
    ],
    "password": ""
}