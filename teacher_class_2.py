import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from classes import Ui_Dialog
from PyQt5.QtWidgets import QListWidgetItem
from server import auth, db


class TeacherClass(QtWidgets.QDialog):

    def __init__(self, login, password):
        super(TeacherClass, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.login = login
        self.password = password


    def init_UI(self):
        self.setWindowTitle("Классы")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())

        self.students = []

        # full list
        #students = ["Елисеев Юрий", "Капустин Юлий", "Филиппов Май", "Назаров Влас", "Быков Трофим", "Лебедев Адриан"]


        #обработчики кнопок
        self.ui.button_show_student.clicked.connect(self.show_student)
        self.ui.button_add_student.clicked.connect(self.add_student)

    def add_element(self, name):
        item = QListWidgetItem()
        item.setIcon(QIcon('student.png'))
        item.setText(name)
        self.ui.listWidget_students.addItem(item)

    def show_student(self):
        #получение класса и буквы
        class_number = self.ui.comboBox_class_number.currentText()
        class_letter = self.ui.comboBox_class_letter.currentText()

        try:
            self.students = []
            #self.ui.listWidget_students.
            user2 = auth.sign_in_with_email_and_password(self.login, self.password)
            all_users = db.child("users").get()
            print(all_users)
            for user in all_users:
                user_new = {'name': '', 'surname': ''}
                if user.val()['profile']['class'] == class_number and user.val()['profile']['letter']:
                    user_new['name'] = user.val()['profile']['name']
                    user_new['surname'] = user.val()['profile']['surname']
                    self.students.append(user_new)
            print(self.students)
            for student in self.students:
                line = student['name'] + " " + student['surname']
                self.add_element(line)
            print(all_users)
        except Exception as e:
            print("Erorr")
            print(e)

        print(class_number, class_letter)

    def add_student(self):
        pass


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    add_achievement = TeacherClass("vanteevs@mail.ru", "testpass")
    add_achievement.show()
    sys.exit(application.exec())

