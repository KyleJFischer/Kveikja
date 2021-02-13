import yaml
import os
import subprocess
import sys
import utils.kConfig as kConfig


KVEIKJA_LOCATION = ''

filePath = ''

#Locations for Immediate Command
commands = {}
keys = []



#Debuging
def printd(input):
    if (kConfig.debugAlwaysOn):
        print(input)

#Loading
def init():
    global KVEIKJA_LOCATION
    KVEIKJA_LOCATION = os.getenv('KVEIKJA_HOME')
    kConfig.init()
    kDatabases.loadProjectDb()
    kDatabases.loadApplicationDb()

def load(fileName):
    global commands, keys
    with open(fileName) as file:
        commands = yaml.full_load(file)
        keys = list(commands)

#MAIN EXECUTABLE
def runKVEIKJA(pathToProjectFile):
    load(pathToProjectFile)
    if kConfig.defaultKeyWord not in keys:
        return False
    for command in commands[kConfig.defaultKeyWord]:
        runCommand(command)

    return True
#Run The Types of Commands
def runCommand(command):
    for item in command:
        lowerCaseCommand = item.lower()
        if (lowerCaseCommand == kConfig.executeKeyWord):
            runExecute(command[item])
        elif (lowerCaseCommand == kConfig.applicationKeyWord):
            runProgram(command[item])
        elif (lowerCaseCommand == kConfig.projectKeyWord):
            runProject(command[item])        

def runExecute(commandDetails):
    os.system(commandDetails['argument'])

def runProgram(commandDetails):
    programName = commandDetails['argument']

    programDetails = getPathFromProgramDb(programName)
    if (programDetails == None):
        print("No Program Found: " + programName)
        return

    subprocess.Popen(programDetails['path'])
    printd('Application Executed: ' +  programDetails['path'])

def runProject(commandDetails):
    projectName = commandDetails['argument']
    runProjectByName(projectName)

def runProjectByName(projectName):
    print()
    projectDetails = getPathFromProjectDb(projectName)
    if (projectDetails == None):
        print("No Project Found: " + projectName)
        return

    runKVEIKJA(projectDetails['path'])
    printd('Project Executed: ' +  projectDetails['path'])






def figureOutIfPath(input):
    return False

if __name__ == "__main__":
    init()
    argumentCount = len(sys.argv)
    
    if (argumentCount == 1):
        runKVEIKJA(".kveikja")
    if (argumentCount == 2):
        runProjectByName(sys.argv[1])