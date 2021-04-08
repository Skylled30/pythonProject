import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from classes import Ui_Dialog
from PyQt5.QtWidgets import QListWidgetItem
from server import auth, db
from editor_for_teacher_class import EditorForTeacher


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

        self.ui.listWidget_students.clear()

        # full list
        #students = ["Елисеев Юрий", "Капустин Юлий", "Филиппов Май", "Назаров Влас", "Быков Трофим", "Лебедев Адриан"]


        #обработчики кнопок
        self.ui.button_show_student.clicked.connect(self.show_student)
        self.ui.button_add_student.clicked.connect(self.add_student)
        self.ui.listWidget_students.clicked.connect(self.open_profile)

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
            self.ui.listWidget_students.clear()
            self.users = db.child("users").get().val()
            print(self.users)

            for user in self.users:
                if self.users[user]["profile"]["type"] == "user" and self.users[user]["profile"]["class"] == class_number \
                        and self.users[user]["profile"]["letter"] == class_letter.lower():
                    name_surname = f'{self.users[user]["profile"]["name"]} {self.users[user]["profile"]["surname"]}'
                    self.add_element(name_surname)

        except Exception as e:
            print("Erorr")
            print(e)

        print(class_number, class_letter)

    def add_student(self):
        pass

    def open_profile(self):
        number_item = self.ui.listWidget_students.currentRow()
        user_id = list(self.users)[number_item]
        self.user = self.users[user_id]
        self.editor_for_teacher = EditorForTeacher(self)
        self.editor_for_teacher.show()


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    add_achievement = TeacherClass("teachercheck@mail.ru", "teachercheck")
    add_achievement.show()
    sys.exit(application.exec())

