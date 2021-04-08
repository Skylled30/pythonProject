import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMessageBox
from list_achievements_gui import Ui_Dialog
import student_profile
import change_achievement
from server import auth, storage, db


class ListAchievements(QtWidgets.QDialog):
    def __init__(self, root):
        super(ListAchievements, self).__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.root = root
        self.login = self.root.login
        self.password = self.root.password
        self.init_UI()
        self.getDataFromFireBase()

    def init_UI(self):
        self.setWindowTitle("Список достижений")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())
        self.ui.button_back.clicked.connect(self.go_back)
        self.ui.listWidget.itemClicked.connect(self.change_achievement)

    def getDataFromFireBase(self):
        try:
            user = auth.sign_in_with_email_and_password(self.login, self.password)
            achievements = db.child('users').child(user['localId']).child('achievements').get()
            data = achievements.val()
            self.dict_achievements = list(data)
            for key in data:
                name = data[key]['competition_name']
                self.add_element(name)
        except Exception:
            print("Error getting data from the server")

    def add_element(self, name):
        item = QListWidgetItem()
        item.setIcon(QIcon('icon_achievement.png'))
        item.setText(name)
        self.ui.listWidget.addItem(item)

    def go_back(self):
        self.close()

    def change_achievement(self):
        number_item = self.ui.listWidget.currentRow()
        self.numberSelectedItem = self.dict_achievements[number_item]
        self.dialog_achievement = change_achievement.ChangeAchievement(self)
        self.dialog_achievement.exec_()
        self.ui.listWidget.clear()
        self.getDataFromFireBase()
if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    list_achievements = ListAchievements()
    list_achievements.show()

    sys.exit(application.exec())
