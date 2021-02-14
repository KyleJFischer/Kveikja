import yaml
import utils.kConfig as kConfig
import utils.kLogger as kLogger
loaded = False

locationOfDb = ''
#Locations for application Database
projectDb = None
projectDbKeys = None

def init(projectDbLocation):
    kLogger.printDebug('Starting Initing of Project Db')
    global locationOfDb
    locationOfDb = projectDbLocation
    loadProjectDb()
    kLogger.printDebug('Done Initing Project Db')

def loadProjectDb():
    global projectDb, projectDbKeys, loaded
    if not loaded:
        with open(locationOfDb) as file:
            projectDb = yaml.full_load(file)
            projectDbKeys = list(projectDb)
            loaded = True

def getPathFromProjectDb(projectName):
    if (projectDb is None):
        init(kConfig.getFullPath('projectDbLocation'))
    if projectName in projectDbKeys:
        projectPath = projectDb[projectName]
        return projectPath

    return None    