# project to develop LOGO UI at home
import sys
import hello
from  PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pass

MainWindow = QMainWindow()
ui = hello.Ui_Form()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
