import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QFileDialog
from editing_achievement import Ui_Dialog
from server import auth, db, storage


class ChangeAchievement(QtWidgets.QDialog):
    def __init__(self, parent):
        super(ChangeAchievement, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.init_UI()
        self.fpath_check = 0
        self.getDataFromFireBase()

    def init_UI(self):
        self.setWindowTitle("Редактирование достижения")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())
        self.fpath = ""

        # вид конкурса
        self.ui.comboBox_competition_type.addItem("Стажировка")
        self.ui.comboBox_competition_type.addItem("Пресс-конференция")
        self.ui.comboBox_competition_type.addItem("Мастер-класс")

        # название конкурса
        self.ui.lineEdit_competition_name.setText("")

        # вид работы
        self.ui.comboBox_type_work.addItem("Выступление")

        # вид документа
        # self.ui.comboBox_type_document.addItem("")

        # дата проведение
        self.ui.dateEdit_event.setDateTime(QtCore.QDateTime.currentDateTime())

        # занятое место
        self.ui.comboBox_place.addItem("Победитель")

        # уровень олимпиады
        # self.ui.comboBox_level_competition.addItem()

        # предмет
        self.ui.comboBox_subject.addItems(["Обществознание", "ОБЖ", "Химия", "Физика", "История", "Немецкий язык", "Музыка", "Черчение"])

        #обработчики кнопок
        self.ui.button_scan.clicked.connect(self.select_file)
        self.ui.button_cancel.clicked.connect(self.go_back)
        self.ui.button_add.clicked.connect(self.update_achievement)
        self.ui.button_delete.clicked.connect(self.delete_achievement)

    def select_file(self):
        try:
            fpath1 = QFileDialog.getOpenFileName(self, 'Выбор файла', '/home')[0]
            self.fpath = fpath1.replace("/", "\\")
            if len(self.fpath) > 1:
                self.fpath_check = 1
                self.button_scan.setText("Скан выбран")
        except Exception as e:
            print(e)

    def getDataFromFireBase(self):
        try:
            login, password, self.key = self.parent.login, self.parent.password, self.parent.numberSelectedItem
            self.user = auth.sign_in_with_email_and_password(login, password)
            achievements = db.child('users').child(self.user['localId']).child('achievements').child(self.key).get()
            print(self.key)
            self.data_achievement = achievements.val()
            self.fill_fields()
        except Exception as e :
            print("getdatafirebase")
            print(e)

    def fill_fields(self):
        self.ui.comboBox_competition_type.setCurrentText(self.data_achievement['competition_type'])
        self.ui.lineEdit_competition_name.setText(self.data_achievement['competition_name'])
        self.ui.comboBox_type_work.setCurrentText(self.data_achievement['work_type'])
        self.ui.comboBox_type_document.setCurrentText(self.data_achievement['type_document'])
        self.ui.comboBox_place.setCurrentText(self.data_achievement['place'])
        self.ui.comboBox_level_competition.setCurrentText(self.data_achievement['level_competition'])
        self.ui.comboBox_subject.setCurrentText(self.data_achievement['subject'])
        self.ui.dateEdit_event.setDate(QDate.fromString(self.data_achievement['date'], 'dd.MM.yyyy').toPyDate())

    def go_back(self):
        self.hide()

    def update_achievement(self):
        competition_type = self.ui.comboBox_type_work.currentText()
        competition_name = self.ui.lineEdit_competition_name.text()
        work_type = self.ui.comboBox_type_work.currentText()
        type_document = self.ui.comboBox_type_document.currentText()
        place = self.ui.comboBox_place.currentText()
        level_competition = self.ui.comboBox_level_competition.currentText()
        subject = self.ui.comboBox_subject.currentText()
        date = self.ui.dateEdit_event.text()
        new_data = {'competition_type': competition_type, 'competition_name': competition_name, 'work_type': work_type,
                    'type_document': type_document, 'place': place, 'level_competition': level_competition,
                    'subject': subject, 'date': date}
        print("new_data", new_data)
        if len(self.fpath) > 1:
            print("103 check if path >1")
            d = self.fpath.split(".")
            file_format = d[-1]
            new_data = {'competition_type': competition_type, 'competition_name': competition_name,
                        'work_type': work_type, 'type_document': type_document,
                        'place': place, 'level_competition': level_competition, 'subject': subject, 'date': date, 'file_format': file_format}
            storage.child("/" + self.user['localId'] + "/" + d[-2] + "." + file_format).put(self.fpath, self.user['idToken'])
    #авторизируемся и обновляем данные
        print("here")
        try:
            db.child('users').child(self.user['localId']).child('achievements').child(self.key).update(new_data)
            print("Update ")
        except Exception as e:
            print("113 change", e)
            print(new_data)

    def delete_achievement(self):
        user = auth.sign_in_with_email_and_password(self.parent.login, self.parent.password)
        try:
            reply = QMessageBox.question(self, 'Предупреждение', 'Удалить достижение?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
            if reply == QMessageBox.Yes:
                student = db.child('users').child(user['localId']).child('profile').get()
                data = student.val()
                achievements = db.child('users').child(user['localId']).child('achievements').get()
                #storage.child("/" + user['localId'] + "/" + key_achievement + "." + file_format).delete(user['idToken'])
                i1 = int(data["countAchievements"])
                i1 -= 1
                data = {"countAchievements": i1}
                db.child('users').child(user["localId"]).child("profile").update(data, user['idToken'])
                db.child('users').child(user['localId']).child('achievements').child(self.key).remove()
                reply = QMessageBox.question(self, 'Успех!', 'Вы успешно удалили достижение',
                                             QMessageBox.Ok)
                self.hide()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    change_achievement = ChangeAchievement(None)
    change_achievement.show()

    sys.exit(application.exec())
