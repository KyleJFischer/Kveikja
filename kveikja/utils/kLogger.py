import utils.kConfig as kConfig

def printDebug(obj):
    if (kConfig.debugAlwaysOn):
        print(str(obj))