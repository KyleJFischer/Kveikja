import yaml
import os
import subprocess
import sys
import commands.project as projectCommand
import utils.kConfig as kConfig
import utils.kLogger as kLogger

#Loading
def init():
    kConfig.init()

if __name__ == "__main__":
    init()
    argumentCount = len(sys.argv)
    kLogger.printDebug('Argument Count: ' + str(argumentCount))
    if (argumentCount == 1):
        projectCommand.ExecuteCommandFile(kConfig.projectFileName)
    if (argumentCount == 2):
        projectCommand.runProjectByName(sys.argv[1])