# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_achievements.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 351)
        self.title_name = QtWidgets.QLabel(Dialog)
        self.title_name.setGeometry(QtCore.QRect(0, 0, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_name.setFont(font)
        self.title_name.setStyleSheet("font: 14pt \"Source Sans Pro\";")
        self.title_name.setAlignment(QtCore.Qt.AlignCenter)
        self.title_name.setObjectName("title_name")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 401, 251))
        self.listWidget.setObjectName("listWidget")
        self.label_count_achievements = QtWidgets.QLabel(Dialog)
        self.label_count_achievements.setGeometry(QtCore.QRect(20, 310, 201, 31))
        self.label_count_achievements.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_count_achievements.setObjectName("label_count_achievements")
        self.button_back = QtWidgets.QPushButton(Dialog)
        self.button_back.setGeometry(QtCore.QRect(270, 310, 151, 31))
        self.button_back.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_back.setObjectName("button_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_name.setText(_translate("Dialog", "Ваши достижения"))
        self.label_count_achievements.setText(_translate("Dialog", "Количество баллов: 10"))
        self.button_back.setText(_translate("Dialog", "Вернуться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
