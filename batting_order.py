# in terminal paste in command below
#"C:\PydroXL_19\envs\Pydro367\Lib\site-packages\PySide2\designer.exe"
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import pickle
# from PySide2.QtWidgets import QMessageBox, QApplication

# Code from Barry Gallagher (available under https://github.com/noaa-ocs-hydrography)
# cheap setup of the python path to see where it is on the local machine
os.environ['PYTHONPATH'] = r"C:\Ib project"
from HSTB.gui import qtGuiConfig
# from HSTB.shared import RegistryHelpers

def load_list(file_location):
    phile = open(file_location, "rb")
    batting_list = pickle.load(phile)
    return batting_list
def save_order(batting_order, file_location):
    phile = open(file_location, "wb")
    pickle.dump(batting_order, phile)
    phile.close()


class BattingOrder:
    """ This is a class to keep team name and passwords together."""
    def __init__(self, batters):
        self.batters = batters
    def duplicate_check(self):
        pass

class BattingOrder(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"batting order.ui"), [])  # , use_registry="connor")
        self.batting_list = []
        #self.batting_list = load_list("c:\\Ib project\\batting order.ui")

        # connect a button to a function
        # self.gui.windows.test_button.clicked.connect(self.print_values)
        self.win.buttonBox.accepted.connect(self.on_press_ok)
        for batter_instance in self.batting_list:
            self.win.player_box.addItem(batter_instance.name)

    def show(self):
        self.win.show()

    def on_press_ok(self):
        print(self.gui.batter1)
        found_name = False
        """
        for search_team in self.batting_list:
            if self.gui.team_box == search_team.name:
                found_name = True
                if self.gui.password_box == search_team.password:
                    print("GOOD FAT BOY")
                else:
                    print("Trash")
        if found_name == False:
            new_team = BattingOrder(self.gui.team_box, self.gui.password_box)
            self.batting_list.append(new_team)
            save_login(self.batting_list,"c:\\Ib project\\BattingOrder")
        """
        """ This function would be called when the test_button is pressed
        """


        
def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    dlg = BattingOrder()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()