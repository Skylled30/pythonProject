import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from profile import Ui_Dialog
import datetime
import adding_achievement
import list_achievements
import make_report
from server import auth, db


class StudentProfile(QtWidgets.QMainWindow):
    def __init__(self, login, password):
        super(StudentProfile, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.login = login
        self.password = password
        self.getDataFromFireBase()



    def init_UI(self):
        self.setWindowTitle("Ваш профиль")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())

        self.date = f"Сегодня: {self.get_date()}"
        self.ui.button_new_achievement.clicked.connect(self.open_window_add_achievement)
        self.ui.button_my_achievements.clicked.connect(self.open_window_my_achievements)
        self.ui.button_make_report.clicked.connect(self.open_window_make_report)

    def getDataFromFireBase(self):
        try:

            user = auth.sign_in_with_email_and_password(self.login, self.password)
            student = db.child('users').child(user['localId']).child('profile').get()
            data = student.val()
            if int(data['countAchievements']) != 0:
                achievements = db.child('users').child(user['localId']).child('achievements').get()
                data = achievements.val()
                i = 0
                for key in data:
                    i += 1
                data2 = {"countAchievements": i}
                db.child('users').child(user["localId"]).child("profile").update(data2, user['idToken'])

            student = db.child('users').child(user['localId']).child('profile').get()
            data = student.val()
            self.fill_fields(data['name'], data['surname'], data['class'], data['letter'], data['countAchievements'])
        except Exception as e:
            print(e)

    def fill_fields(self, name_user, surname_user, class_number_user, letter_user, count_achievements):
        self.ui.label_name_user.setText(name_user)
        self.ui.label_surname_user.setText(surname_user)
        self.ui.label_class_number_user.setText(class_number_user)
        self.ui.label_letter_user.setText(letter_user)
        self.ui.label_count_achievements.setText(f'Количество достижений: {count_achievements}')
        self.ui.label_date.setText(self.date)

    def get_date(self):
        d = datetime.date.today()
        day = d.day
        month = d.month - 1
        a = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября',
             'Декабря']
        return f"{day} {a[month % 12]}"

    def open_window_add_achievement(self):
        self.dialog = adding_achievement.AddAchievement(self)
        self.hide()
        self.dialog.exec()
        self.show()
        self.getDataFromFireBase()

    def open_window_my_achievements(self):
        self.dialog = list_achievements.ListAchievements(self)
        self.hide()
        self.dialog.exec()
        self.show()
        self.getDataFromFireBase()
    def open_window_make_report(self):
        self.dialog = make_report.MakeReport(self, self.login, self.password)
        self.hide()
        self.dialog.exec()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Предупреждение', 'Закрыть программу?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.No:
            event.ignore()


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    # studentProfile = StudentProfile("vanteevs@mail.ru", "testpass")
    studentProfile = StudentProfile("po4tapo4ta@mail.ru", "po4tapo4ta@mail.ru")
    studentProfile.show()

    sys.exit(application.exec())
