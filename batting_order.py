# in terminal paste in command below
#"C:\PydroXL_19\envs\Pydro367\Lib\site-packages\PySide2\designer.exe"
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import pickle
import player_editor
import game_sim
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
        self.drawing = PainterWidget(self.gui.windows.graphicsView)  # put a widget on top of the graphics area
        # connect a button to a function
        self.gui.windows.start_game.clicked.connect(self.simulate)
        self.player_list = player_editor.load_list("c:\\Ib project\\player_editor.db")
        self.batting_list = load_list("c:\\Ib project\\BattingOrder.pickle")

        # connect a button to a function
        # self.gui.windows.test_button.clicked.connect(self.print_values)
        self.win.buttonBox.accepted.connect(self.on_press_ok)
        for player_name in self.player_list:
            for i in range(1,10):
                self.gui.windows["batter" + str(i)].addItem(player_name)
            self.win.eh.addItem(player_name)
        print(self.batting_list)
        [self.gui.batter1, self.gui.batter2, self.gui.batter3, self.gui.batter4, self.gui.batter5,
         self.gui.batter6, self.gui.batter7, self.gui.batter8, self.gui.batter9, self.gui.eh] = self.batting_list
    def simulate(self):
        self.batting_list = [self.gui.batter1, self.gui.batter2, self.gui.batter3, self.gui.batter4, self.gui.batter5,
                             self.gui.batter6, self.gui.batter7, self.gui.batter8, self.gui.batter9, self.gui.eh]
        sr = 0
        for game in range(1,163):
            tr = game_sim.game(self.batting_list)
            #print (tr)
            sr += tr
            #sr is season runs
        print (sr/162)
    def show(self):
        self.win.show()

    def on_press_ok(self):
        self.batting_list = [self.gui.batter1, self.gui.batter2, self.gui.batter3, self.gui.batter4, self.gui.batter5,
                             self.gui.batter6, self.gui.batter7, self.gui.batter8, self.gui.batter9, self.gui.eh]
        save_order(self.batting_list, "c:\\Ib project\\BattingOrder.pickle")
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

from PySide2.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QFileDialog,
    QStyle,
    QAction,
    QColorDialog,
)
from PySide2.QtCore import Qt, Slot, QStandardPaths
from PySide2.QtGui import (
    QMouseEvent,
    QPaintEvent,
    QPen,
    QPainter,
    QColor,
    QPixmap,
    QIcon,
    QKeySequence,
    QStaticText,
)

# pulled from QT docs at https://doc.qt.io/qtforpython/examples/example_widgets_painting_painter.html
# modified to run under PySide2 (instead of PySide6)
# added text and rectangle examples.
class PainterWidget(QtWidgets.QWidget):
    """A widget where user can draw with their mouse

    The user draws on a QPixmap which is itself paint from paintEvent()

    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(680, 480)
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.white)
        self.painter = QPainter()

        self.painter.begin(self.pixmap)
        self.painter.fillRect(0,0,50,50, Qt.blue)
        self.painter.end()

    def paintEvent(self, event: QPaintEvent):
        """Override method from QWidget

        Paint the Pixmap into the widget

        """
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def draw_name(self):
        self.painter.begin(self.pixmap)
        self.painter.fillRect(0,0,50,50, Qt.green)
        self.painter.drawStaticText(10,10, QStaticText("Connor"))
        self.painter.end()
        self.update()

    def clear(self):
        """ Clear the pixmap """
        self.pixmap.fill(Qt.white)
        self.update()


class Login(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"example.ui"), [])  # , use_registry="connor")
        self.drawing = PainterWidget(self.gui.windows.graphicsView)  # put a widget on top of the graphics area
        # connect a button to a function
        self.gui.windows.test_button.clicked.connect(self.print_values)


    def show(self):
        self.win.show()
        self.drawing

    def print_values(self):
        """ This function would be called when the test_button is pressed
        """
        # we can access values using self.gui.name_from_designer
        # the guiconfig module translates that to the appropriate commands for get/set of the values in whatever the object on screen is
        print(1, self.gui.plainTextEdit)
        # self.win is the thing that QT would give you back using the "loader" function on the .ui fil
        # and you would have to find the text widget and either remember it or search every time
        for ch in self.win.children():
            if ch.objectName() == "plainTextEdit":
                print(2, ch.toPlainText())
        # but guiconfig also extends the self.win object so you can use the name from qtdesigner
        print(3, self.win.plainTextEdit.toPlainText())
        # and here is the combobox value
        print(self.gui.comboBox)
        # using the self.gui naming, we can also change a value like it's a variable using guiconfig
        self.gui.plainTextEdit = "override the text value"
        # use the window (self.win) show how to add options to the dropdown part of the combobox
        # see the docs for a qt combobox at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QComboBox.html
        self.win.comboBox.addItems(['barry', 'connor'])
        if 1:
            self.gui.comboBox = 'my new name'
        else:
            self.win.comboBox.setCurrentText("new name")
        painter = QtGui.QPainter(self.gui.windows.test_button)
        painter.fillRect(0, 0, 128, 128, Qt.green)
        painter = QtGui.QPainter(self.win)
        painter.fillRect(0, 0, 128, 128, Qt.green)


        
def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    dlg = BattingOrder()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
