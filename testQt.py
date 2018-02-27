import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        self.resize(250,150)
        self.setWindowTitle('Statusbar')
        
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QApplication.instance().quit)
        btn.move(50,50)

        self.show()

if __name__ == '__main__':
    app = QtCore.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
