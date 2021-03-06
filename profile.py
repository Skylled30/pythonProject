# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 239)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 30, 491, 16))
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.title_name = QtWidgets.QLabel(Dialog)
        self.title_name.setGeometry(QtCore.QRect(0, -1, 261, 41))
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
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(250, 0, 20, 251))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(30, 50, 51, 21))
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
        self.label_count_achievements = QtWidgets.QLabel(Dialog)
        self.label_count_achievements.setGeometry(QtCore.QRect(10, 170, 201, 31))
        self.label_count_achievements.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_count_achievements.setObjectName("label_count_achievements")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 160, 261, 16))
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_name_user = QtWidgets.QLabel(Dialog)
        self.label_name_user.setGeometry(QtCore.QRect(90, 50, 151, 21))
        self.label_name_user.setStyleSheet("font: 11pt \"Source Sans Pro\";\n"
"border: 1px solid ;")
        self.label_name_user.setObjectName("label_name_user")
        self.label_surname_user = QtWidgets.QLabel(Dialog)
        self.label_surname_user.setGeometry(QtCore.QRect(90, 80, 151, 21))
        self.label_surname_user.setStyleSheet("font: 11pt \"Source Sans Pro\";\n"
"border: 1px solid ;")
        self.label_surname_user.setObjectName("label_surname_user")
        self.label_class_number_user = QtWidgets.QLabel(Dialog)
        self.label_class_number_user.setGeometry(QtCore.QRect(90, 110, 151, 21))
        self.label_class_number_user.setStyleSheet("font: 11pt \"Source Sans Pro\";\n"
"border: 1px solid ;")
        self.label_class_number_user.setObjectName("label_class_number_user")
        self.label_letter_user = QtWidgets.QLabel(Dialog)
        self.label_letter_user.setGeometry(QtCore.QRect(90, 140, 151, 21))
        self.label_letter_user.setStyleSheet("font: 11pt \"Source Sans Pro\";\n"
"border: 1px solid ;")
        self.label_letter_user.setObjectName("label_letter_user")
        self.label_place_rating = QtWidgets.QLabel(Dialog)
        self.label_place_rating.setGeometry(QtCore.QRect(10, 200, 201, 31))
        self.label_place_rating.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.label_place_rating.setObjectName("label_place_rating")
        self.button_new_achievement = QtWidgets.QPushButton(Dialog)
        self.button_new_achievement.setGeometry(QtCore.QRect(280, 50, 181, 51))
        self.button_new_achievement.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_new_achievement.setObjectName("button_new_achievement")
        self.label_date = QtWidgets.QLabel(Dialog)
        self.label_date.setGeometry(QtCore.QRect(310, 0, 160, 41))
        self.label_date.setStyleSheet("font: 12pt \"Source Sans Pro\";")
        self.label_date.setObjectName("label_date")
        self.button_my_achievements = QtWidgets.QPushButton(Dialog)
        self.button_my_achievements.setGeometry(QtCore.QRect(280, 110, 181, 51))
        self.button_my_achievements.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_my_achievements.setObjectName("button_my_achievements")
        self.button_make_report = QtWidgets.QPushButton(Dialog)
        self.button_make_report.setGeometry(QtCore.QRect(280, 170, 181, 51))
        self.button_make_report.setStyleSheet("font: 11pt \"Source Sans Pro\";")
        self.button_make_report.setObjectName("button_make_report")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_name.setText(_translate("Dialog", "?????? ??????????????"))
        self.label_name.setText(_translate("Dialog", "??????"))
        self.label_surname.setText(_translate("Dialog", "??????????????"))
        self.label_class.setText(_translate("Dialog", "??????????"))
        self.label_letter.setText(_translate("Dialog", "??????????"))
        self.label_count_achievements.setText(_translate("Dialog", "???????????????????? ????????????????????: 10"))
        self.label_name_user.setText(_translate("Dialog", "????????"))
        self.label_surname_user.setText(_translate("Dialog", "????????????"))
        self.label_class_number_user.setText(_translate("Dialog", "10"))
        self.label_letter_user.setText(_translate("Dialog", "??"))
        self.label_place_rating.setText(_translate("Dialog", "?????????? ?? ????????????????: 5"))
        self.button_new_achievement.setText(_translate("Dialog", "?????????? ????????????????????"))
        self.label_date.setText(_translate("Dialog", "??????????????: 21 ??????????????"))
        self.button_my_achievements.setText(_translate("Dialog", "?????? ????????????????????"))
        self.button_make_report.setText(_translate("Dialog", "???????????????????????? ????????????"))

