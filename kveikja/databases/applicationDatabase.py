import yaml
from utils import kConfig

loaded = False

locationOfDb = ''
#Locations for application Database
applicationDb = None
applicationDbKeys = None


def init(applicationDbLocation):
    global locationOfDb
    locationOfDb = applicationDbLocation
    loadApplicationDb()

def loadApplicationDb():
    global applicationDb, applicationDbKeys, loaded 
    if not loaded:
        with open(locationOfDb) as file:
            applicationDb = yaml.full_load(file)
            applicationDbKeys = list(applicationDb)
            loaded = True

def getPathFromApplicationDb(programName):
    if (applicationDbKeys == None):
        appDbLocation = kConfig.getFullPath('applicationDbLocation')
        init(appDbLocation)
    if programName in applicationDbKeys:
        return applicationDb[programName]

    return None   
