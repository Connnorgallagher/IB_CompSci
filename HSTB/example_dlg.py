import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QMessageBox, QApplication
# from HSTB.shared import RegistryHelpers

# Code from Barry Gallagher (available under https://github.com/noaa-ocs-hydrography)
# cheap setup of the python path to see where it is on the local machine
os.environ['PYTHONPATH'] = r"C:\Programs\python_code\ConnorProject"
from HSTB.gui import qtGuiConfig

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

        self.previous_pos = None
        self.painter = QPainter()
        self.pen = QPen()
        self.pen.setWidth(10)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.RoundJoin)
        self.painter.begin(self.pixmap)
        self.painter.fillRect(0,0,50,50, Qt.blue)
        # self.painter.drawStaticText(10,10, QStaticText("Connor"))
        self.painter.end()

    def paintEvent(self, event: QPaintEvent):
        """Override method from QWidget

        Paint the Pixmap into the widget

        """
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

    def mousePressEvent(self, event: QMouseEvent):
        """Override from QWidget

        Called when user clicks on the mouse

        """
        self.previous_pos = event.pos()  # event.position().toPoint()
        self.painter.begin(self.pixmap)
        self.painter.fillRect(0,0,50,50, Qt.green)
        # self.painter.drawStaticText(10,10, QStaticText("Connor"))
        self.painter.end()
        QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """Override method from QWidget

        Called when user moves and clicks on the mouse

        """
        current_pos = event.pos()  # event.position().toPoint()
        self.painter.begin(self.pixmap)
        self.painter.setRenderHints(QPainter.Antialiasing, True)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self.previous_pos, current_pos)
        # self.painter.fillRect(0,0,50,50, Qt.green)
        # self.painter.drawStaticText(10,10, QStaticText("Connor"))
        self.painter.end()

        self.previous_pos = current_pos
        self.update()

        QWidget.mouseMoveEvent(self, event)

    def draw_name(self):
        self.painter.begin(self.pixmap)
        self.painter.drawStaticText(10,10, QStaticText("Connor"))
        self.painter.end()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Override method from QWidget

        Called when user releases the mouse

        """
        self.previous_pos = None
        self.draw_name()
        QWidget.mouseReleaseEvent(self, event)

    def save(self, filename: str):
        """ save pixmap to filename """
        self.pixmap.save(filename)

    def load(self, filename: str):
        """ load pixmap from filename """
        self.pixmap.load(filename)
        self.pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio)
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
    dlg = Login()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
