# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up_student_by_teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 222)
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(90, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_surname = QtWidgets.QLabel(Dialog)
        self.label_surname.setGeometry(QtCore.QRect(20, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_surname.setFont(font)
        self.label_surname.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_surname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_surname.setObjectName("label_surname")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-10, 30, 271, 16))
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("font: 14pt \"Source Sans Pro\";")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.lineEdit_surname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_surname.setGeometry(QtCore.QRect(90, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_surname.setFont(font)
        self.lineEdit_surname.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.lineEdit_surname.setText("")
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.label_letter = QtWidgets.QLabel(Dialog)
        self.label_letter.setGeometry(QtCore.QRect(20, 140, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_letter.setFont(font)
        self.label_letter.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_letter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_letter.setObjectName("label_letter")
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setGeometry(QtCore.QRect(20, 180, 101, 31))
        self.button_cancel.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_cancel.setObjectName("button_cancel")
        self.label_class = QtWidgets.QLabel(Dialog)
        self.label_class.setGeometry(QtCore.QRect(20, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_class.setFont(font)
        self.label_class.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_class.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_class.setObjectName("label_class")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(20, 50, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.button_add = QtWidgets.QPushButton(Dialog)
        self.button_add.setGeometry(QtCore.QRect(130, 180, 101, 31))
        self.button_add.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_add.setObjectName("button_add")
        self.comboBox_class_number_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_class_number_2.setGeometry(QtCore.QRect(90, 110, 41, 25))
        self.comboBox_class_number_2.setObjectName("comboBox_class_number_2")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_number_2.addItem("")
        self.comboBox_class_letter = QtWidgets.QComboBox(Dialog)
        self.comboBox_class_letter.setGeometry(QtCore.QRect(90, 140, 41, 25))
        self.comboBox_class_letter.setObjectName("comboBox_class_letter")
        self.comboBox_class_letter.addItem("")
        self.comboBox_class_letter.addItem("")
        self.comboBox_class_letter.addItem("")
        self.comboBox_class_letter.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_surname.setText(_translate("Dialog", "??????????????"))
        self.label_title.setText(_translate("Dialog", "??????????????????????"))
        self.label_letter.setText(_translate("Dialog", "??????????"))
        self.button_cancel.setText(_translate("Dialog", "????????????"))
        self.label_class.setText(_translate("Dialog", "??????????"))
        self.label_name.setText(_translate("Dialog", "??????"))
        self.button_add.setText(_translate("Dialog", "????????????????"))
        self.comboBox_class_number_2.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_class_number_2.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_class_number_2.setItemText(2, _translate("Dialog", "3"))
        self.comboBox_class_number_2.setItemText(3, _translate("Dialog", "4"))
        self.comboBox_class_number_2.setItemText(4, _translate("Dialog", "5"))
        self.comboBox_class_number_2.setItemText(5, _translate("Dialog", "6"))
        self.comboBox_class_number_2.setItemText(6, _translate("Dialog", "7"))
        self.comboBox_class_number_2.setItemText(7, _translate("Dialog", "8"))
        self.comboBox_class_number_2.setItemText(8, _translate("Dialog", "9"))
        self.comboBox_class_number_2.setItemText(9, _translate("Dialog", "10"))
        self.comboBox_class_number_2.setItemText(10, _translate("Dialog", "11"))
        self.comboBox_class_letter.setItemText(0, _translate("Dialog", "??"))
        self.comboBox_class_letter.setItemText(1, _translate("Dialog", "??"))
        self.comboBox_class_letter.setItemText(2, _translate("Dialog", "??"))
        self.comboBox_class_letter.setItemText(3, _translate("Dialog", "??"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
