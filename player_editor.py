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

def load_list(file_location):
    team_list = []
    phile = open(file_location, "r")
    for record in phile.readlines():
        team,password = record.split()
        team_list.append(TeamPass(team,password))
    return team_list
def save_login(team_info, file_location):
    phile = open(file_location, "w")
    for team in team_info:
        phile.write(team.as_string())


class TeamPass:
    """ This is a class to keep team name and passwords together."""
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def as_string(self):
        val = f"{self.name} {self.password}\n"
        return val
    def read_string(self, data):
        self.name , self.password = data.split()

class PlayerEditor(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"Player_editor.ui"), [])  # , use_registry="connor")
        #self.team_list = load_list("c:\\Ib project\\")

        # connect a button to a function
        # self.gui.windows.test_button.clicked.connect(self.print_values)
        self.win.buttonBox.accepted.connect(self.on_press_ok)
        for player_instance in self.player_list:
            self.win.player_box.addItem(player_instance.name)

    def show(self):
        self.win.show()

    def on_press_ok(self):
        found_name = False
        for search_team in self.team_list:
            if self.gui.team_box == search_team.name:
                found_name = True
                if self.gui.password_box == search_team.password:
                    print("GOOD FAT BOY")
                else:
                    print("Trash")
        if found_name == False:
            new_team = TeamPass(self.gui.team_box, self.gui.password_box)
            self.team_list.append(new_team)
            save_login(self.team_list,"c:\\Ib project\\TeamPass")
        """ This function would be called when the test_button is pressed
        """


        
def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    dlg = PlayerEditor()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
