import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtWidgets import QMessageBox, QApplication

# Code from Barry Gallagher (available under https://github.com/noaa-ocs-hydrography)
# cheap setup of the python path to see where it is on the local machine
os.environ['PYTHONPATH'] = r"C:\Programs\python_code\ConnorProject"
from HSTB.gui import qtGuiConfig
# from HSTB.shared import RegistryHelpers


class Login(qtGuiConfig.guiconfig_mixin):
    def __init__(self):
        """ The __init__ does the start/setup and we are using the guiconfig module to make the ui code cleaner+easier
        """
        # this loads a QT designer .ui file and creates some convenience functions and access names
        qtGuiConfig.guiconfig_mixin.__init__(self, os.path.join(os.path.split(__file__)[0], r"example.ui"), [])  # , use_registry="connor")
        # connect a button to a function
        self.gui.windows.test_button.clicked.connect(self.print_values)

    def show(self):
        self.win.show()

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

        
def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    dlg = Login()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
