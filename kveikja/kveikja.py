import yaml
import os
import subprocess
import sys
import utils.kConfig as kConfig
import databases.applicationDatabase as appDb
import databases.projectDatabase as projDb
import utils.commandManager as cmdManager
import utils.kLogger as kLogger

#Locations for Immediate Command
commands = {}
keys = []


#Loading
def init():
    kConfig.init()

def loadCommandFile(fileName):
    global commands, keys
    with open(fileName) as file:
        commands = yaml.full_load(file)
        keys = list(commands)

def runProject(commandDetails):
    projectName = commandDetails['argument']
    runProjectByName(projectName)

def runProjectByName(projectName):
    projectDetails = projDb.getPathFromProjectDb(projectName)
    if (projectDetails == None):
        print("No Project Found: " + projectName)
        return

    ExecuteCommandFile(projectDetails['path'])

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


if __name__ == "__main__":
    init()
    argumentCount = len(sys.argv)
    kLogger.printDebug('Arguement Count: ' + str(argumentCount))
    if (argumentCount == 1):
        ExecuteCommandFile(kConfig.projectFileName)
    if (argumentCount == 2):
        runProjectByName(sys.argv[1])