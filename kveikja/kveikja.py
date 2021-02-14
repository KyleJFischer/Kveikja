import yaml
import os
import subprocess
import sys
import utils.kConfig as kConfig
import databases.applicationDatabase as appDb
import databases.projectDatabase as projDb
import utils.commandManager as cmdManager
import utils.kLogger as kLogger
KVEIKJA_LOCATION = ''

filePath = ''

#Locations for Immediate Command
commands = {}
keys = []


#Loading
def init():
    global KVEIKJA_LOCATION
    KVEIKJA_LOCATION = os.getenv('KVEIKJA_HOME')
    kConfig.init()

def load(fileName):
    global commands, keys
    with open(fileName) as file:
        commands = yaml.full_load(file)
        keys = list(commands)

#MAIN EXECUTABLE
def runKVEIKJA(pathToProjectFile):
    kLogger.printDebug('Loading Project File: ' + pathToProjectFile)
    load(pathToProjectFile)
    if kConfig.defaultKeyWord not in keys:
        kLogger.printDebug('Couldnt Find Default KeyWord')
        return False
    kLogger.printDebug('Executing Commands')    
    for command in commands[kConfig.defaultKeyWord]:
        cmdManager.runCommand(command)

    return True
 


def runProgram(commandDetails):
    programName = commandDetails['argument']

    programDetails = appDb.getPathFromApplicationDb(programName)
    if (programDetails == None):
        print("No Program Found: " + programName)
        return

    subprocess.Popen(programDetails['path'])
    printd('Application Executed: ' +  programDetails['path'])

def runProject(commandDetails):
    projectName = commandDetails['argument']
    runProjectByName(projectName)

def runProjectByName(projectName):
    projDb.init
    projectDetails = projDb.getPathFromProjectDb(projectName)
    if (projectDetails == None):
        print("No Project Found: " + projectName)
        return

    runKVEIKJA(projectDetails['path'])


if __name__ == "__main__":
    init()
    argumentCount = len(sys.argv)
    kLogger.printDebug('Arguement Count: ' + str(argumentCount))
    if (argumentCount == 1):
        runKVEIKJA(kConfig.projectFileName)
    if (argumentCount == 2):
        runProjectByName(sys.argv[1])