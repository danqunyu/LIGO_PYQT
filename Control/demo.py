# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LIGOPlatform(object):
    def setupUi(self, LIGOPlatform):
        LIGOPlatform.setObjectName("LIGOPlatform")
        LIGOPlatform.resize(1314, 880)
        self.centralwidget = QtWidgets.QWidget(LIGOPlatform)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 400, 811, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.lo_Instance = QtWidgets.QGridLayout(self.layoutWidget)
        self.lo_Instance.setContentsMargins(0, 0, 0, 0)
        self.lo_Instance.setObjectName("lo_Instance")
        self.InstanceList = QtWidgets.QLabel(self.layoutWidget)
        self.InstanceList.setTextFormat(QtCore.Qt.RichText)
        self.InstanceList.setObjectName("InstanceList")
        self.lo_Instance.addWidget(self.InstanceList, 0, 0, 1, 5)
        self.InstancceListView = QtWidgets.QListView(self.layoutWidget)
        self.InstancceListView.setObjectName("InstancceListView")
        self.lo_Instance.addWidget(self.InstancceListView, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.lo_Instance.addWidget(self.label_4, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lo_Instance.addItem(spacerItem, 2, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.lo_Instance.addWidget(self.listView, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.lo_Instance.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.lo_Instance.addWidget(self.label_2, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lo_Instance.addItem(spacerItem1, 2, 3, 1, 1)
        self.listView_2 = QtWidgets.QListView(self.layoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.lo_Instance.addWidget(self.listView_2, 2, 4, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(581, 41, 321, 316))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.lo_Program = QtWidgets.QGridLayout(self.layoutWidget1)
        self.lo_Program.setContentsMargins(0, 0, 0, 0)
        self.lo_Program.setObjectName("lo_Program")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.lo_Program.addWidget(self.label_5, 2, 0, 1, 1)
        self.Program = QtWidgets.QLabel(self.layoutWidget1)
        self.Program.setObjectName("Program")
        self.lo_Program.addWidget(self.Program, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.lo_Program.addWidget(self.label_3, 1, 0, 1, 1)
        self.listView_3 = QtWidgets.QListView(self.layoutWidget1)
        self.listView_3.setObjectName("listView_3")
        self.lo_Program.addWidget(self.listView_3, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.lo_Program.addWidget(self.label_6, 3, 0, 1, 1)
        self.listView_4 = QtWidgets.QListView(self.layoutWidget1)
        self.listView_4.setObjectName("listView_4")
        self.lo_Program.addWidget(self.listView_4, 2, 2, 1, 1)
        self.listView_6 = QtWidgets.QListView(self.layoutWidget1)
        self.listView_6.setObjectName("listView_6")
        self.lo_Program.addWidget(self.listView_6, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lo_Program.addItem(spacerItem2, 1, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 12, 431, 327))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.lo_TestMethod = QtWidgets.QGridLayout(self.layoutWidget2)
        self.lo_TestMethod.setContentsMargins(0, 0, 0, 0)
        self.lo_TestMethod.setObjectName("lo_TestMethod")
        self.TestMethodView = QtWidgets.QGridLayout()
        self.TestMethodView.setObjectName("TestMethodView")
        self.cb_TestMethodLib = QtWidgets.QComboBox(self.layoutWidget2)
        self.cb_TestMethodLib.setStyleSheet("font: 12pt \"Arial\";")
        self.cb_TestMethodLib.setObjectName("cb_TestMethodLib")
        self.cb_TestMethodLib.addItem("")
        self.cb_TestMethodLib.addItem("")
        self.cb_TestMethodLib.addItem("")
        self.cb_TestMethodLib.addItem("")
        self.TestMethodView.addWidget(self.cb_TestMethodLib, 1, 0, 1, 1)
        self.TestMethodLib = QtWidgets.QLabel(self.layoutWidget2)
        self.TestMethodLib.setObjectName("TestMethodLib")
        self.TestMethodView.addWidget(self.TestMethodLib, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TestMethodView.addItem(spacerItem3, 0, 1, 1, 1)
        self.lo_TestMethod.addLayout(self.TestMethodView, 0, 0, 1, 1)
        self.ArgumentsView = QtWidgets.QGridLayout()
        self.ArgumentsView.setObjectName("ArgumentsView")
        self.Arg3 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg3.setObjectName("Arg3")
        self.ArgumentsView.addWidget(self.Arg3, 2, 0, 1, 1)
        self.Arg4 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg4.setObjectName("Arg4")
        self.ArgumentsView.addWidget(self.Arg4, 3, 0, 1, 1)
        self.ArgDescription_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_2.setObjectName("ArgDescription_2")
        self.ArgumentsView.addWidget(self.ArgDescription_2, 1, 2, 1, 1)
        self.Arg2 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg2.setObjectName("Arg2")
        self.ArgumentsView.addWidget(self.Arg2, 1, 0, 1, 1)
        self.ArgDescription_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_3.setObjectName("ArgDescription_3")
        self.ArgumentsView.addWidget(self.ArgDescription_3, 2, 2, 1, 1)
        self.ArgValue_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_7.setObjectName("ArgValue_7")
        self.ArgumentsView.addWidget(self.ArgValue_7, 6, 4, 1, 1)
        self.ArgDescription_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_7.setObjectName("ArgDescription_7")
        self.ArgumentsView.addWidget(self.ArgDescription_7, 6, 2, 1, 1)
        self.ArgDescription_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_8.setObjectName("ArgDescription_8")
        self.ArgumentsView.addWidget(self.ArgDescription_8, 7, 2, 1, 1)
        self.ArgDescription_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_4.setObjectName("ArgDescription_4")
        self.ArgumentsView.addWidget(self.ArgDescription_4, 3, 2, 1, 1)
        self.ArgValue_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_3.setObjectName("ArgValue_3")
        self.ArgumentsView.addWidget(self.ArgValue_3, 2, 4, 1, 1)
        self.ArgValue_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_2.setObjectName("ArgValue_2")
        self.ArgumentsView.addWidget(self.ArgValue_2, 1, 4, 1, 1)
        self.ArgDescription_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_5.setObjectName("ArgDescription_5")
        self.ArgumentsView.addWidget(self.ArgDescription_5, 4, 2, 1, 1)
        self.ArgValue_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_4.setObjectName("ArgValue_4")
        self.ArgumentsView.addWidget(self.ArgValue_4, 3, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ArgumentsView.addItem(spacerItem4, 0, 1, 1, 1)
        self.Arg5 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg5.setObjectName("Arg5")
        self.ArgumentsView.addWidget(self.Arg5, 4, 0, 1, 1)
        self.ArgValue_1 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_1.setObjectName("ArgValue_1")
        self.ArgumentsView.addWidget(self.ArgValue_1, 0, 4, 1, 1)
        self.ArgValue_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_5.setObjectName("ArgValue_5")
        self.ArgumentsView.addWidget(self.ArgValue_5, 4, 4, 1, 1)
        self.ArgDescription_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_6.setObjectName("ArgDescription_6")
        self.ArgumentsView.addWidget(self.ArgDescription_6, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ArgumentsView.addItem(spacerItem5, 0, 3, 1, 1)
        self.ArgValue_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_6.setObjectName("ArgValue_6")
        self.ArgumentsView.addWidget(self.ArgValue_6, 5, 4, 1, 1)
        self.Arg7 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg7.setObjectName("Arg7")
        self.ArgumentsView.addWidget(self.Arg7, 6, 0, 1, 1)
        self.Arg6 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg6.setObjectName("Arg6")
        self.ArgumentsView.addWidget(self.Arg6, 5, 0, 1, 1)
        self.ArgValue_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgValue_8.setObjectName("ArgValue_8")
        self.ArgumentsView.addWidget(self.ArgValue_8, 7, 4, 1, 1)
        self.Arg1 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg1.setObjectName("Arg1")
        self.ArgumentsView.addWidget(self.Arg1, 0, 0, 1, 1)
        self.ArgDescription_1 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ArgDescription_1.setObjectName("ArgDescription_1")
        self.ArgumentsView.addWidget(self.ArgDescription_1, 0, 2, 1, 1)
        self.Arg8 = QtWidgets.QLabel(self.layoutWidget2)
        self.Arg8.setObjectName("Arg8")
        self.ArgumentsView.addWidget(self.Arg8, 7, 0, 1, 1)
        self.lo_TestMethod.addLayout(self.ArgumentsView, 1, 0, 1, 1)
        self.AddAsInstancce = QtWidgets.QPushButton(self.layoutWidget2)
        self.AddAsInstancce.setObjectName("AddAsInstancce")
        self.lo_TestMethod.addWidget(self.AddAsInstancce, 2, 0, 1, 1)
        LIGOPlatform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LIGOPlatform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1314, 26))
        self.menubar.setObjectName("menubar")
        LIGOPlatform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LIGOPlatform)
        self.statusbar.setObjectName("statusbar")
        LIGOPlatform.setStatusBar(self.statusbar)

        self.retranslateUi(LIGOPlatform)
        QtCore.QMetaObject.connectSlotsByName(LIGOPlatform)

    def retranslateUi(self, LIGOPlatform):
        _translate = QtCore.QCoreApplication.translate
        LIGOPlatform.setWindowTitle(_translate("LIGOPlatform", "MainWindow"))
        self.InstanceList.setToolTip(_translate("LIGOPlatform", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Instance List &amp; Arguments</span></p></body></html>"))
        self.InstanceList.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#5555ff;\">Instance List &amp; Arguments &amp; Flow Generation</span></p></body></html>"))
        self.label_4.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Flow Selection</span></p></body></html>"))
        self.label.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">All Available Instrances</span></p></body></html>"))
        self.label_2.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Related Arguments</span></p></body></html>"))
        self.label_5.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Main</span></p><p align=\"center\"><span style=\" font-weight:600;\">Flow</span></p></body></html>"))
        self.Program.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff00ff;\">Final Program</span></p></body></html>"))
        self.label_3.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Dynamic</span></p><p align=\"center\"><span style=\" font-weight:600;\">Preload</span></p></body></html>"))
        self.label_6.setText(_translate("LIGOPlatform", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Unload</span></p></body></html>"))
        self.cb_TestMethodLib.setItemText(0, _translate("LIGOPlatform", "Search"))
        self.cb_TestMethodLib.setItemText(1, _translate("LIGOPlatform", "StartPoint"))
        self.cb_TestMethodLib.setItemText(2, _translate("LIGOPlatform", "Backoff"))
        self.cb_TestMethodLib.setItemText(3, _translate("LIGOPlatform", "LimitLine"))
        self.TestMethodLib.setText(_translate("LIGOPlatform", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#55aa00;\">Test Method Lib</span></p></body></html>"))
        self.Arg3.setText(_translate("LIGOPlatform", "Arg3"))
        self.Arg4.setText(_translate("LIGOPlatform", "Arg4"))
        self.Arg2.setText(_translate("LIGOPlatform", "Arg2"))
        self.Arg5.setText(_translate("LIGOPlatform", "Arg5"))
        self.Arg7.setText(_translate("LIGOPlatform", "Arg7"))
        self.Arg6.setText(_translate("LIGOPlatform", "Arg6"))
        self.Arg1.setText(_translate("LIGOPlatform", "Arg1"))
        self.Arg8.setText(_translate("LIGOPlatform", "Arg8"))
        self.AddAsInstancce.setText(_translate("LIGOPlatform", "Add As Instance"))