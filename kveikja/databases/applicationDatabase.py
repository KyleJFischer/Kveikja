import yaml

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
        with open(os.path.join(KVEIKJA_LOCATION, kConfig.applicationDbLocation)) as file:
            applicationDb = yaml.full_load(file)
            applicationDbKeys = list(applicationDb)
            loaded = True


def getPathFromApplicationDb(programName):
    if (applicationDbKeys == None):
        loadApplicationDb()
    if programName in applicationDbKeys:
        return applicationDb[programName]

    return None   
