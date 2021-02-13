import yaml
import os

#CONST
CONFIG_LOCATION = r'resources\config.yaml'
KVEIKJA_LOCATION = ''

loaded = False
debugAlwaysOn = False

#Defaults In case Config File isn't There
defaultKeyWord = 'launch'
executeKeyWord = 'execute'
applicationKeyWord = 'application'
projectKeyWord = 'project'

#Database Locations
applicationDbLocation = r'resources\programDb.yaml'
projectDbLocation = r'resources\projectDb.yaml'

#Project Files
projectFileName = r'.kveikja'

def init():
    global loaded, KVEIKJA_LOCATION
    if (not loaded):
        KVEIKJA_LOCATION = os.getenv('KVEIKJA_HOME')
        location = os.path.join(KVEIKJA_LOCATION, CONFIG_LOCATION)
        loadConfigSettings(location)
        loaded = True

def loadConfigSettings(location):
    global applicationDbLocation, projectDbLocation
    print('ourLocation', location)
    with open(location) as file:
        config = yaml.full_load(file)
        loadSettingsFromConfig(config)
        loadKeyWordsFromConfig(config)
        loadDatabaseLocationsFromConfig(config)
    return config

def loadSettingsFromConfig(config):
    global projectFileName, debugAlwaysOn
    debugAlwaysOn = config['debugAlwaysOn']
    projectFileName = config['projectFileName']

def loadKeyWordsFromConfig(config):
    global defaultKeyWord, executeKeyWord, applicationKeyWord, projectKeyWord  
    defaultKeyWord = config['defaultKeyWord']
    executeKeyWord = config['executeKeyWord']
    applicationKeyWord = config['applicationKeyWord']
    projectKeyWord = config['projectKeyWord']
    
def loadDatabaseLocationsFromConfig(config):
    global applicationDbLocation, projectDbLocation
    applicationDbLocation = config['applicationDbLocation']
    projectDbLocation = config['projectDbLocation']