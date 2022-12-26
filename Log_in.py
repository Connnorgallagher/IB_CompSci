# in terminal paste in command below
#"C:\PydroXL_19\envs\Pydro367\Lib\site-packages\PySide2\designer.exe"
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtWidgets import QMessageBox, QApplication

# Code from Barry Gallagher (available under https://github.com/noaa-ocs-hydrography)
# cheap setup of the python path to see where it is on the local machine
os.environ['PYTHONPATH'] = r"C:\Ib project"
from HSTB.gui import qtGuiConfig
# from HSTB.shared import RegistryHelpers
def save_login(team_info, file_location):
    open(file_location, "w").write("trash")
#team_info = {'Oakland': 'Luigi'}
#team_info['Baltimore'] = "dad"

class TeamPass:
   ...:     def __init__(self, name, password):
   ...:         self.name = name
   ...:         self.password = password
   ...:     def as_String(self):
   ...:         val = f"{self.name} {self.password}\n"
   ...:         return val
   ...:     def read_string(self, data):
   ...:         self.name , self.password = data.split()
B = TeamPass("seattle", "Trash")
In[8]: phile = open("c:\\Ib project\\TeamPass", "w")
  ...: phile.write(A.as_String())
  ...: phile.write(B.as_String())
  ...: phile.close()
  s = A.as_String()
  oak,p = s.split()
  phile = open("c:\\Ib project\\TeamPass", "r")
phile.readlines()
    """ This is a class to keep team name and passwords together."""
class Login(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"Log_in.ui"), [])  # , use_registry="connor")
        # connect a button to a function
        # self.gui.windows.test_button.clicked.connect(self.print_values)
        self.win.buttonBox.accepted.connect(self.on_press_ok)
        self.win.team.addItems(list(team_info.keys()))

    def show(self):
        self.win.show()

    def on_press_ok(self):
        if self.gui.team not in team_info:
            team_info[self.gui.team] = self.gui.password
            save_login(team_info)
        """ This function would be called when the test_button is pressed
        """
        # we can access values using self.gui.name_from_designer
        # the guiconfig module translates that to the appropriate commands for get/set of the values in whatever the object on screen is
        print(1, self.gui.password)
        # self.win is the thing that QT would give you back using the "loader" function on the .ui fil
        # and you would have to find the text widget and either remember it or search every time
        for ch in self.win.children():
            if ch.objectName() == "password":
                print(2, ch.toPlainText())
        # but guiconfig also extends the self.win object so you can use the name from qtdesigner
        print(3, self.win.password.toPlainText())
        # and here is the team value
        print(self.gui.team)
        # using the self.gui naming, we can also change a value like it's a variable using guiconfig
        self.gui.password = "override the text value"
        # use the window (self.win) show how to add options to the dropdown part of the team
        # see the docs for a qt combo box at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/Qcombobox.html
        self.win.team.addItems(['barry', 'connor'])
        if 1:
            self.gui.team = 'my new name'
        else:
            self.win.team.setCurrentText("new name")

        
def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    dlg = Login()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
