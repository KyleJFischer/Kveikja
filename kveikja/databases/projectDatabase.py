import yaml

loaded = False

locationOfDb = ''
#Locations for application Database
projectDb = None
projectDbKeys = None

def init(projectDbLocation):
    global locationOfDb
    locationOfDb = projectDbLocation
    loadProjectDb()

def loadProjectDb():
    global projectDb, projectDbKeys, loaded
    if not loaded:
        with open(locationOfDb) as file:
            projectDb = yaml.full_load(file)
            projectDbKeys = list(projectDb)
            loaded = True


def getPathFromProjectDb(projectName):
    if projectName in projectDbKeys:
        return projectDb[projectName]

    return None    