# virtualBBQduck - Your Virtual assistant
Welcome to virtualBBQduck.

virtualBBQduck runs in the background and you can ask it to do many things.
You can even program your own functions.

Be carefull not to make a function to delete System32😉

### Run

Use run.py to run it normally.

Use runAsync.py to run it with threading, being able to run commands in the background.

## my todo list:
- import command packs
- update default commands using Update command
- add param to loadDefaultCommands to auto import imported commands
    - also work with updated commands
- import and update to preset only
- presets functionality:
    - saving preset
    - loading preset
    - programming preset
    - preset memory
        - sentance -> command converter
        - replace parts of command with memorized data
        - ask something that it knows
    - autosave preset memory
- critical windows file protection (basics work)
- password for creating a new command
- password for overwriting default command
- filtering simular to projectsviewer to "list" command
- global effects
- global memory
- global commands
- getMetaData
    - importHandler.getLibraries()
    - importHandler.getLibraryData(name)
    - preset.handler.getPresets()
    - preset.handler.getPresetData(name)
- commands that do the following:
    - send messages to the connected device
    - ask connected device to do something for me
    - commands to add things to memory
    - commands to forceClose a thread
    - commands to disconnect from server / switch server
    - putting reminders
    - edititng reminders
    - changing list of commands allowed to be used by client connected on server
- list of commands allowed to be used by client connected on server
- reference commands: dh -> help, dl -> list
- run commands before running them, for logging or quest systems