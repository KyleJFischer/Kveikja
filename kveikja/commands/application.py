import ..databases.applicationDatabase as applicationDb


def runProgram(commandDetails):
    applicationDb.loadApplicationDb()

    programDetails = applicationDb.getPathFromApplicationDb(programName)
    if (programDetails == None):
        print("No Program Found: " + programName)
        return

    subprocess.Popen(programDetails['path'])
    printd('Application Executed: ' +  programDetails['path'])