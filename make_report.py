import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from make_report_gui import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog
import student_profile
import os
import server
from server import db, storage, auth
import zipfile
from datetime import *
class MakeReport(QtWidgets.QDialog):
    def __init__(self, root, login, password):
        super(MakeReport, self).__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()
        self.login = login
        self.password = password
        self.root = root
        self.i = 0

    def init_UI(self):
        self.setWindowTitle("Формирование отчёта")
        # self.setWindowIcon(QIcon("note_icon.png"))
        self.setFixedSize(self.size())
        # вид конкурса
        self.type = self.ui.comboBox_competition_type.currentText()
        # название отчёта
        self.name = self.ui.lineEdit_competition_name.text()

        # вид работы
        self.work_type = self.ui.comboBox_type_work.currentText()

        # вид документа
        self.type_document = self.ui.comboBox_type_document.currentText()

        # дата проведение             self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateEdit_to.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateEdit_from.setDateTime(QtCore.QDateTime.currentDateTime())

        # занятое место
        self.place = self.ui.comboBox_place.currentText()

        # уровень олимпиады
        self.level = self.ui.comboBox_level_competition.currentText()

        # предмет
        self.subject = self.ui.comboBox_subject.currentText()

        #обработчики событий
        self.ui.button_cancel.clicked.connect(self.go_back)
        self.ui.pushButton_3.clicked.connect(self.get_text)




    def get_text(self):
        # try:
        print("gettext")
        self.user = server.auth.sign_in_with_email_and_password(self.login, self.password)
        student = server.db.child("users").child(self.user['localId']).child("achievements").get()
        data = student.val()
        self.achievements = data

        if self.ui.checkBox_scan.isChecked():
            QMessageBox.warning(self, 'Выберите путь сохранения сканов!', 'Выберите путь сохранения сканов')
            self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку для сохранения")
            self.download_folder.replace("/", "\\")
            self.zip = zipfile.ZipFile(f'{self.download_folder}/{self.ui.lineEdit_competition_name.text()}.zip', 'w', zipfile.ZIP_DEFLATED)  # создаем архив
            self.my_file = open(f'{self.download_folder}/{self.ui.lineEdit_competition_name.text()}.txt', "w+")
        else:
            QMessageBox.warning(self, 'Выберите путь сохранения отчёта!', 'Выберите путь сохранения отчёта')
            self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать путь сохранения отчёта")
            self.download_folder.replace("/", "\\")
            self.my_file = open(f'{self.download_folder}/{self.ui.lineEdit_competition_name.text()}.txt', "w+")




        for key in data:
            self.name_comp = data[key]['competition_name']
            self.type_comp = data[key]['competition_type']
            self.level_comp = data[key]["level_competition"]
            self.place_comp = data[key]["place"]
            self.subject_comp= data[key]["subject"]
            self.type_doc_comp = data[key]["type_document"]
            self.work_comp = data[key]["work_type"]
            self.date_comp = data[key]['date']
            date1 = data[key]['date'] #29.12.2020
            datee = date1.split(".")
            day, month, year = int(datee[0]), int(datee[1]), int(datee[2])
            given_date = date(int(year), int(month), int(day))
            self.dateEdit_to = self.ui.self.dateEdit_to.text().split(".")
            self.dateEdit_from = self.ui.self.dateEdit_from.text().split(".")
            from_date = date(self.dateEdit_from[0], self.dateEdit_from[1], self.dateEdit_from[2])
            to_date = date(self.dateEdit_to[0], self.dateEdit_to[1], self.dateEdit_to[2])
            # if (self.level != 'Не выбрано ' and self.level == level) and (
            #         self.place != 'Не выбрано ' and self.place == place)
            print(given_date)
            print(date)
            print(from_date)
            print(to_date)
            if given_date >= from_date and given_date <= to_date:
                print('get_in date')
                if (self.type == self.type_comp or self.type_comp == "Не выбрано") and (self.level_comp == level or self.level_comp == "Не выбрано") and \
                        (self.place_comp == place or self.place_comp == "Не выбрано")\
                        and (self.subject_comp == subject or self.subject_comp == "Не выбрано") and\
                        (self.type_comp == type_document or self.type_comp == "Не выбрано")\
                        and (self.work_comp == work_type or self.work_comp == "Не выбрано"):
                    print('get_in big check 1')
                    if self.ui.checkBox_scan.isChecked():
                        self.save_scan(key)
                    self.my_file.write("Название конкурса: " + self.name + "\n")
                    self.my_file.write("Тип конкурса: " + self.type + "\n")
                    self.my_file.write("Дата проведения конкурса: " + self.date + "\n")
                    self.my_file.write("Занятое место: " + self.place + "\n")
                    self.my_file.write("Предмет конкурса: " + self.subject + "\n")
                    self.my_file.write("Тип документа: " + self.type_document + "\n")
                    self.my_file.write("Тип работы: " + self.work_type + "\n")
                    self.my_file.write("Уровень конкурса: " + self.level + "\n")

                    self.my_file.write("\n" + "\n" + "\n")




        self.my_file.close()
        if self.ui.checkBox_scan.isChecked():
            new_arch = f'{self.download_folder}/{self.ui.lineEdit_competition_name.text()}.txt'
            self.zip.write(new_arch, f"{self.ui.lineEdit_competition_name.text()}.txt")
            self.zip.close()

            QMessageBox.question(self, 'Успех!', 'Отчёт и сканы созданы в выбранной папке',
                                         QMessageBox.Ok)
        else:

            QMessageBox.question(self, 'Успех!', 'Отчёт создан в выбранной папке',
                                 QMessageBox.Ok)
        self.close()
        # except Exception as e:
        #     reply = QMessageBox.question(self, 'Провал!', 'Произошла ошибка!',
        #                                  QMessageBox.Ok)
        #     print(e)
        #     print("Error get_text")

    def go_back(self):
        self.close()
    def save_scan(self, key):
        #брать key из гет текста и передавать его
        if self.ui.checkBox_scan.isChecked():
            d = self.user['localId'] #upper token, profile token
            achievements = db.child('users').child(self.user['localId']).child('achievements').get()
            data = achievements.val()
            try:
                upper_path = f'{d}/'
                file_name_base = f'{key}.{data[key]["file_format"]}'
                file_format = data[key]["file_format"]
                storage.child(f"{upper_path}{file_name_base}").download(f"{self.download_folder}/",
                                                                               f"{self.download_folder}/{self.name}.{file_format}",
                                                                               token=self.user['idToken'])

                new_arch = f'{self.download_folder}/{self.name}.{file_format}'
                self.zip.write(new_arch, f"{self.name}.{file_format}")
                os.remove(f"{self.download_folder}/{self.name}.{file_format}")
            except Exception as e:
                print(e)
                print("Except save_scan")

if __name__ == "__main__":
    application = QtWidgets.QApplication([])
    # studentProfile = StudentProfile("vanteevs@mail.ru", "testpass")
    studentProfile = student_profile.StudentProfile("po4tapo4ta@mail.ru", "po4tapo4ta@mail.ru")
    studentProfile.show()

    sys.exit(application.exec())
