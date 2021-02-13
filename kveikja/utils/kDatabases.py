import kConfig

#Locations for application Database
applicationDb = None
applicationDbKeys = None

#Locations for Project Database
projectDb = None
projectDbKeys = None

def loadApplicationDb():
    global applicationDb, applicationDbKeys
    printd("Loading Program DB")
    print(kConfig.applicationDbLocation)
    with open(os.path.join(KVEIKJA_LOCATION, kConfig.applicationDbLocation)) as file:
        applicationDb = yaml.full_load(file)
        applicationDbKeys = list(applicationDb)


def loadProjectDb():
    global projectDb, projectDbKeys
    printd("Loading Project DB")
    print(KVEIKJA_LOCATION, kConfig.projectDbLocation)
    with open(os.path.join(KVEIKJA_LOCATION, kConfig.projectDbLocation)) as file:
        projectDb = yaml.full_load(file)
        projectDbKeys = list(projectDb)