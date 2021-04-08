import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from add_achievement import Ui_Dialog
import datetime
from PyQt5.QtWidgets import QFileDialog
from server import auth, db, storage
import json
class AddAchievement(QtWidgets.QDialog):

    def __init__(self, root):
        super(AddAchievement, self).__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.main = root
        self.fpath = 0
    def init_UI(self):
        self.setWindowTitle("Добавление достижения")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())

        #вид конкурса
        self.ui.comboBox_competition_type.addItem("Стажировка")
        self.ui.comboBox_competition_type.addItem("Пресс-конференция")
        self.ui.comboBox_competition_type.addItem("Мастер-класс")

        #название конкурса
        self.ui.lineEdit_competition_name.setText("")

        #вид работы
        self.ui.comboBox_type_work.addItem("Выступление")

        #вид документа
        # self.ui.comboBox_type_document.addItem("")

        #дата проведение
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        #занятое место
        self.ui.comboBox_place.addItem("Победитель")

        #уровень олимпиады
        # self.ui.comboBox_level_competition.addItem()

        #предмет
        self.ui.comboBox_subject.addItems(["Обществознание", "ОБЖ", "Химия", "Физика", "История", "Немецкий язык", "Музыка", "Черчение"])

        #обработка кнопок
        self.ui.button_scan.clicked.connect(self.select_file)
        self.ui.button_cancel.clicked.connect(self.go_back)
        self.ui.button_add.clicked.connect(self.add_achievement_to_firebase)


    def go_back(self):
        self.close()

    def select_file(self):
        fpath1 = QFileDialog.getOpenFileName(self, 'Выбор файла', '/home')[0]
        self.fpath = fpath1.replace("/", "\\")
        self.ui.button_scan.setText("Скан выбран")
    def add_achievement_to_firebase(self):
        user = auth.sign_in_with_email_and_password(self.main.login, self.main.password)
        try:
            student = db.child('users').child(user['localId']).child('profile').get()
            data = student.val()
            i1 = int(data["countAchievements"])
            i1 += 1
            data = {"countAchievements": i1}
            if self.fpath != 0:
                d = self.fpath.split(".")
                file_format = d[-1]
                # storage.child("image3/").download("C:\\", user['idToken'])
                achievement = {"competition_type": self.ui.comboBox_competition_type.currentText(),
                               "competition_name": self.ui.lineEdit_competition_name.text(),
                               "work_type": self.ui.comboBox_type_work.currentText(),
                               "type_document": self.ui.comboBox_type_document.currentText(),
                               "date": self.ui.dateEdit.text(),
                               "place": self.ui.comboBox_place.currentText(),
                               "level_competition": self.ui.comboBox_level_competition.currentText(),
                               "subject": self.ui.comboBox_subject.currentText(),
                               'file_format': file_format}
                db.child('users').child(user['localId']).child('achievements').push(achievement)
                achievements = db.child('users').child(user['localId']).child('achievements').get()
                data3 = achievements.val()
                name = self.ui.lineEdit_competition_name.text()
                for key in data3:
                    name2 = data3[key]['competition_name']
                    if name2 == name:
                        key_achievement = key
                storage.child("/" + user['localId'] + "/" + key_achievement + "." + file_format).put(self.fpath, user['idToken'])
                db.child('users').child(user["localId"]).child("profile").update(data, user['idToken'])
                reply = QMessageBox.question(self, 'Успех!', 'Вы успешно добавили достижение', QMessageBox.Ok,
                                             QMessageBox.Ok)
                self.hide()
            else:
                reply = QMessageBox.warning(self, 'Неудача!', 'Вы не добавили путь до скана!')
                self.select_file

                self.add_achievement_to_firebase
        except BaseException as e:
            QMessageBox.warning(self, 'Предупреждение', 'Произошла ошибка при добавления достижения')
            print("Произошла ошибка при загрузке достижения")
            print(f'Error: {e}')


if __name__ == "__main__":
    application = QtWidgets.QApplication([])

    add_achievement = AddAchievement(None)
    add_achievement.show()
    sys.exit(application.exec())
