# project to develop LOGO UI at home
import sys
import LIGOPlatform
# import hello
from PyQt5.QtWidgets import QApplication,QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.ui = LIGOPlatform.Ui_LIGOPlatform()
        # self.ui.startUi()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mainWindow = MainForm()
    # mainWindow.show()

    mainwindow  = QMainWindow()
    ui = LIGOPlatform.Ui_LIGOPlatform()
    ui.startUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())


    # MainWindow = QMainWindow()
    # ui = hello.Ui_Form()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    pass
