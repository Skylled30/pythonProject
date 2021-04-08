import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from add_achievement import Ui_Dialog
import datetime
from PyQt5.QtWidgets import QFileDialog
from server import auth, db


class AddAchievement(QtWidgets.QDialog):

    def __init__(self, root):
        super(AddAchievement, self).__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.main = root

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
        fpath = QFileDialog.getOpenFileName(self, 'Выбор файла', '/home')[0]
        print(fpath)

    def add_achievement_to_firebase(self):
        user = auth.sign_in_with_email_and_password(self.main.login, self.main.password)
        try:
            achievement = {"competition_type": self.ui.comboBox_competition_type.currentText(), "competition_name": self.ui.lineEdit_competition_name.text(), "work_type": self.ui.comboBox_type_work.currentText(),
                           "type_document": self.ui.comboBox_type_document.currentText(), "date": self.ui.dateEdit.text(), "place": self.ui.comboBox_place.currentText(), "level_competition": self.ui.comboBox_level_competition.currentText(),
                           "subject": self.ui.comboBox_subject.currentText(), "scan": "image/1.pdf"}
            results = db.child('users').child(user['localId']).child('achievements').push(achievement)
            reply = QMessageBox.question(self, 'Заметка', 'Вы успешно добавили достижение', QMessageBox.No,
                                         QMessageBox.No)
            self.close()
        except BaseException as e:
            QMessageBox.warning(self, 'Предупреждение', 'Произошла ошибка при добавления достижения')
            print("Произошла ошибка при загрузке достижения")
            print(f'Error: {e}')


if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    add_achievement = AddAchievement(None)
    add_achievement.show()
    sys.exit(application.exec())
