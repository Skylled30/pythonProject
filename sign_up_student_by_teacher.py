import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from sign_up_student_by_teacher_gui import Ui_Dialog
from PyQt5.QtWidgets import QListWidgetItem
from server import db, auth
import teacher_class
import random
class AddStudent(QtWidgets.QDialog):
    def __init__(self, login, password):
        super(AddStudent, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.login = login
        self.password = password
        self.user = auth.sign_in_with_email_and_password(self.login, self.password)
    def init_UI(self):
        self.setWindowTitle("Классы")
        self.ui.button_cancel.clicked.connect(self.close)
        self.ui.button_add.clicked.connect(self.add_student)
    def add_student(self):
        name = self.ui.lineEdit_name.text()
        surname = self.ui.lineEdit_surname.text()
        sclass = self.ui.comboBox_class_number_2.currentText()
        letter = self.ui.comboBox_class_letter.currentText()
        profile = {"name": name, "surname": surname, "class": sclass, "letter": letter}
        d = db.child('users').child(self.user["localId"]).child("profile").get()
        data = d.val()
        fname_teacher = data['name']
        surname_teacher = data['surname']
        name_teacher = f"{fname_teacher} {surname_teacher}"
        chars = '1234567890'
        for n in range(1):
            hash = ''
            for i in range(6):
                hash += random.choice(chars)
        profile = {"name": name_teacher, "hash": hash, "student": profile}

        db.child('hash').child(hash).set(profile, self.user['idToken'])

        QMessageBox.question(self, 'Успех!', f'Вы успешно зарегистрировали ученика. Его уникальный код регистрации - {hash}',
                                     QMessageBox.Ok)
        self.close()
    def close(self):
        self.close()
if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    teacher_class = AddStudent("teachercheck@mail.ru", "teachercheck")
    teacher_class.show()

    sys.exit(application.exec())


