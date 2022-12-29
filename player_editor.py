# in terminal paste in command below
#"C:\PydroXL_19\envs\Pydro367\Lib\site-packages\PySide2\designer.exe"
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtWidgets import QMessageBox, QApplication
import sqlite3
import os


# Code from Barry Gallagher (available under https://github.com/noaa-ocs-hydrography)
# cheap setup of the python path to see where it is on the local machine
os.environ['PYTHONPATH'] = r"C:\Ib project"
from HSTB.gui import qtGuiConfig
# from HSTB.shared import RegistryHelpers

def load_list(file_location):
    player_all = {}
    conn = sqlite3.connect(file_location)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM players").fetchall()
    for player in data:
        player_all[player["name"]] = player
    return player_all
def save_players(player_stats, file_location):
    conn = sqlite3.connect(file_location)
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE players (name text, number integer, PA integer, B1 integer, B2 integer, B3 integer, B4 integer, "
                    "BB integer, HBP integer, SO integer)")
    except:
        pass
    cur.execute("insert into players values(?, ?, ?,?, ?,?, ?,?, ?,?)", ["connor", 18, 25,3,2,1,4,5,2,1])
    conn.commit()
    for player in player_stats.values():
         cur.execute("insert into players values(?, ?, ?,?, ?,?, ?,?, ?,?)", [player["name"], player["number"], player["PA"],
                                                                              player["B1"],player["B2"],player["B3"],
                                                                              player["B4"],player["BB"],player["HBP"],player["SO"]])
    conn.commit()



class PlayerEditor(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"Player_editor.ui"), [])  # , use_registry="connor")
        self.stat_dict = load_list("c:\\Ib project\\player_editor.db")

        # connect a button to a function
        # self.gui.windows.test_button.clicked.connect(self.print_values)
        self.win.buttonBox.accepted.connect(self.on_press_ok)
        for player_name in self.stat_dict:
            self.win.player_box.addItem(player_name)

    def show(self):
        self.win.show()

    def on_press_ok(self):
        self.stat_dict[self.gui.name_box] = {"name": self.gui.name_box, "PA": self.gui.PA_box,
                                             "number": self.gui.number_box,
                                             "B1": self.gui.B1_box, "B2": self.gui.B2_box,
                                             "B3": self.gui.B3_box, "B4": self.gui.B4_box,
                                             "BB": self.gui.BB_box,
                                             "HBP": self.gui.HBP_box, "SO": self.gui.SO_box}
        save_players(self.stat_dict, "c:\\Ib project\\player_editor.db")
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
