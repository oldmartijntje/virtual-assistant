import models.commands as commands

descriptions = commands.descriptions

libraries = {
    "Funpack": {
        "metaData": {
            "name": "Funpack",
            "author": "OldMartijntje",
            "version": "1.0.0",
            "description": "Fun commands"
        },
        "commands": {
            "cowSay": {
                "function": "import handlers.textHandler as textHandler;import cowsay;textHandler.textController(cowsay.{}(\"{}\"), chatEffect = {}, feedback = True)",
                "parameters": {
                    "var1": {
                        "given": "-animal",
                        "default": "cow",
                        "description": "Animal that displays message.",
                        "options": ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux']
                    },
                    "var2": {
                        "given": "-txt",
                        "default": "Hello World!",
                        "description": "Text to display."
                    },
                    "var3": {
                        "default": "True",
                        "given": "-chatEffect",
                        "description": descriptions["chatEffect"],
                        "options": ["True", "False"]
                    }
                },
                "category": ["Funpack", "effects"],
                "description": "Display a message in a cow.",
                "metaData": {
                    "name": "CowSay command.",
                    "author": "OldMartijntje",
                    "version": "1.0.0",
                    "description": "Using the https://pypi.org/project/cowsay/ library."
                }
            }
        }
    }
}

librariesList = list(libraries.keys())