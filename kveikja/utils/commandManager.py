import utils.kConfig as kConfig
import commands.execute as execute
import commands.project as project
import commands.application as application
import commands.website as website
import utils.kLogger as kLogger
#Run The Types of Commands


def runCommands(command):
    for item in command:
        kLogger.printDebug('Running Command: ' + item)
        lowerCaseCommand = item.lower()
        if (lowerCaseCommand == kConfig.executeKeyWord):
            execute.runCommand(command[item])
        elif (lowerCaseCommand == kConfig.applicationKeyWord):
            application.runProgram(command[item])
        elif (lowerCaseCommand == kConfig.websiteKeyWord):
            website.runCommand(command[item])
        elif (lowerCaseCommand == kConfig.projKeyWord):
            project.runProject(command[item])    
