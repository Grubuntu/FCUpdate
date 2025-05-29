from PySide import QtGui
## The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
import FreeCAD as App
# import FreeCADGui as Gui


def runStartupMacros(name):
    # Do not run when NoneWorkbench is activated because UI isn't yet completely there
    if name != "NoneWorkbench":
        # Run macro only once by disconnecting the signal at first call
        Gui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)

        # Following 2 lines shall be duplicated for each macro to run
        import CheckUpdate
        CheckUpdate.run()

        # Eg. if a second macro shall be launched at startup
        # import MyWonderfulMacro
        # MyWonderfulMacro.run()

# The following 2 lines are important because InitGui.py files are passed to the exec() function...
# ...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
import __main__
__main__.runStartupMacros = runStartupMacros

# Connect the function that runs the macro to the appropriate signal
Gui.getMainWindow().workbenchActivated.connect(runStartupMacros)