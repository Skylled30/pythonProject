import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from editor_for_teacher import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog
from server import auth, db, storage


class EditorForTeacher(QtWidgets.QDialog):
    def __init__(self, root):
        super(EditorForTeacher, self).__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main = root
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Ваш класс")
        self.setFixedSize(self.size())

        self.ui.label_student_name.setText(self.main.user['profile']['name'])
        self.ui.label_class_name.setText(self.main.user['profile']['letter'])
        self.ui.label_student_surname.setText(self.main.user['profile']['surname'])
        self.ui.label_num_class.setText(self.main.user['profile']['class'])
        count_achiv = 'Количество достижений: ' + str(self.main.user['profile']['countAchievements'])
        self.ui.count_achiv.setText(count_achiv)
        label_place_rating = 'Место в рейтинге: ' + str(50)
        self.ui.label_place_in_rating.setText(label_place_rating)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = EditorForTeacher(None)
    application.show()
    sys.exit(app.exec())

