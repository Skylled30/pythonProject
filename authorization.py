import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from login_2 import Ui_Dialog
import student_profile, teacher_class_2, sign_up_student
from server import auth, db, storage
#C:\Users\vante\PycharmProjects\student_portfolio


class Authorization(QtWidgets.QDialog):
    def __init__(self):
        super(Authorization, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowTitle("Авторизация")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())
        self.ui.input_login.setText("po4tapo4ta@mail.ru")
        self.ui.input_password.setText("po4tapo4ta@mail.ru")
        #обработчики кнопок
        self.ui.button_sign_in.clicked.connect(self.sign_in)
        self.ui.button_sign_up.clicked.connect(self.sign_up)

    def sign_in(self):
        login, password = self.ui.input_login.text(), self.ui.input_password.text()
        if self.check_account(login, password):
            type_user = db.child('users').child(self.user['localId']).child('profile').get()
            data = type_user.val()
            if data['type'] == "user":
                self.win_student_profile = student_profile.StudentProfile(login, password)
                self.win_student_profile.show()
                self.close()
            elif data['type'] == "teacher":
                self.win_teacher_class = teacher_class_2.TeacherClass(login, password)
                self.win_teacher_class.show()
                self.close()
    def sign_up(self):
        self.sign_up_student = sign_up_student.SignUpStudent()
        self.sign_up_student.show()
        self.close()

    def check_account(self, login, password):
        try:
            self.user = auth.sign_in_with_email_and_password(login, password)
            return True
        except BaseException as e:
            print(e)
            QMessageBox.warning(self, 'Предупреждение', 'Неправильный логин или пароль!')
            return False


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    authorization = Authorization()
    authorization.show()
    sys.exit(application.exec())
