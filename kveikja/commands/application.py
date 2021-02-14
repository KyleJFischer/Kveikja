import databases.applicationDatabase as applicationDb
import subprocess
import utils.kLogger as kLogger
def runProgram(commandDetails):
    print(commandDetails)
    programDetails = applicationDb.getPathFromApplicationDb(commandDetails['argument'])
    if (programDetails == None):
        print("No Program Found: " + programName)
        return

    subprocess.Popen(programDetails['path'])
    kLogger.printDebug('Application Executed: ' +  programDetails['path'])