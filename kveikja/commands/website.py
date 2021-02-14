import yaml
import webbrowser
#Locations for Immediate Command

def runCommand(commandDetails):
    webbrowser.open(commandDetails['argument'], new=2)
