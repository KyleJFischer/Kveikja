import commands.execute as execute
import utils.kConfig as kConfig
import commands.application as application
import utils.kLogger as kLogger
#Run The Types of Commands
loaded = False
exeKeyWord = ''
appKeyWord = ''
def init():
    global exeKeyWord, appKeyWord
    exeKeyWord = kConfig.executeKeyWord
    appKeyWord = kConfig.applicationKeyWord
    loaded = True

def runCommand(command):
    if (not loaded):
        init()
    for item in command:
        kLogger.printDebug('Running Command: ' + item)
        lowerCaseCommand = item.lower()
        if (lowerCaseCommand == exeKeyWord):
            execute.runCommand(command[item])
        elif (lowerCaseCommand == appKeyWord):
            application.runProgram(command[item])
