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
                "function": "import cowsay;textHandler.textController(cowsay.{}(\"{}\"), chatEffect = {}, feedback = True)",
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
                        "description": "Cow to be used"
                    },
                    "var3": {
                        "default": "True",
                        "given": "-chatEffect",
                        "description": descriptions["chatEffect"],
                        "options": ["True", "False"]
                    }
                },
                "category": ["Funpack", "effects"],
                "description": "Display a message in a cow",
            }
        }
    }
}

librariesList = list(libraries.keys())