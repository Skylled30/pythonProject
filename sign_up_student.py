import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from sign_up_student_gui import Ui_Dialog
from server import auth, db, storage
import student_profile
class SignUpStudent(QtWidgets.QDialog):

    def __init__(self):
        super(SignUpStudent, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Регистрация")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())

        # обработчики кнопок
        self.ui.button_cancel.clicked.connect(self.go_back)
        self.ui.button_add.clicked.connect(self.sign_up_student_to_firebase)

    def sign_up_student_to_firebase(self):
        try:
            input_code = self.ui.lineEdit_code.text()
            data1 = db.child('hash').get()
            data = data1.val()
            check = 0
            for check_code in data:
                code = data[check_code]['hash']
                if str(input_code) == str(code):
                    check = 1
                    password = self.ui.lineEdit_password.text()
                    login = self.ui.lineEdit_email.text()
                    auth.create_user_with_email_and_password(login, password)
                    user = auth.sign_in_with_email_and_password(login, password)
                    student1 = db.child('hash').child(check_code).child('student').get()
                    student = student1.val()
                    profile = {"email": login, "name": student["name"], "surname": student["surname"], "class": student["class"], "letter": student["letter"], "countAchievements": "0", "type": "user"}
                    db.child('users').child(user["localId"]).child("profile").set(profile, user['idToken'])
                    db.child('hash').child(code).remove()
                    reply = QMessageBox.question(self, 'Успех!', 'Вы успешно зарегистрировались',
                                         QMessageBox.Ok)
                    self.close()
                    self.win_student_profile = student_profile.StudentProfile(login, password)
                    self.win_student_profile.show()
            if check == 0:
                reply = QMessageBox.question(self, 'Неудача!', 'Код неверен',
                                         QMessageBox.Ok)

        except Exception as e:
            print(e)
            reply = QMessageBox.question(self, 'Ошибка!', "Аккаунт уже зарегистрирован, неверно введена почта или пароль слишком слабый",
                                     QMessageBox.Ok)
            print("sign_up_student_to_firebase")

    def go_back(self):
        self.close()


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    add_achievement = SignUpStudent()
    add_achievement.show()
    sys.exit(application.exec())
