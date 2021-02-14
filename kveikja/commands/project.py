import yaml
import utils.kConfig as kConfig
import databases.projectDatabase as projDb
import utils.commandManager as cmdManager
import utils.kLogger as kLogger
#Locations for Immediate Command
commands = {}
keys = []

def runProject(commandDetails):
    projectName = commandDetails['argument']
    runProjectByName(projectName)

def runProjectByName(projectName):
    projectDetails = projDb.getPathFromProjectDb(projectName)
    if (projectDetails == None):
        print("No Project Found: " + projectName)
        return

    ExecuteCommandFile(projectDetails['path'])

def loadCommandFile(fileName):
    global commands, keys
    with open(fileName) as file:
        commands = yaml.full_load(file)
        keys = list(commands)


#MAIN EXECUTABLE
def ExecuteCommandFile(pathToProjectFile):
    kLogger.printDebug('Loading Project File: ' + pathToProjectFile)
    loadCommandFile(pathToProjectFile)
    if kConfig.defaultKeyWord not in keys:
        kLogger.printDebug('Couldnt Find Default KeyWord')
        return False
    kLogger.printDebug('Executing Commands')    
    for command in commands[kConfig.defaultKeyWord]:
        cmdManager.runCommands(command)

    return True