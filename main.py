import pyrebase
import random
import time
import string
firebaseConfig = {
    'apiKey': "AIzaSyCtqWOd1gcXuDH3cFUdQzxj8Ii6f4f9zS4",
    'authDomain': "authstudent2.firebaseapp.com",
    'databaseURL': "https://authstudent2.firebaseio.com",
    'projectId': "authstudent2",
    'storageBucket': "authstudent2.appspot.com",
    'messagingSenderId': "1087868700511",
    'appId': "1:1087868700511:web:f869ca3561ab845c5418ea",
    'measurementId': "G-XP68GE315L"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

# def sign_up():
#     email = input("Enter email: ")
#     password = input("Enter password: ")
#     user = auth.create_user_with_email_and_password(email, password)
#     print("Successfully created account!")
#
# def sign_in():
#     pass


# sign_up()
# sign_in()

email = "po4tapo4ta@mail.ru"  # input("Enter email: ")
password = "po4tapo4ta@mail.ru"  # input("Enter password: ")
# email = "123123@mail.ru"  # input("Enter email: ")
# password = "123123123"  # input("Enter password: ")

# print(user)


# try / except
try:
    user = auth.sign_in_with_email_and_password(email, password)
    print("Авторизация прошла успешно!")
except BaseException:
    print("Произошла ошибка, проверьте логин и пароль!")

#добавление данных для ученика set()

#profile_teacher = db.child('users').child(user['localId']).child('profile').get()
#data = profile_teacher.val()
#profile = {"фамилия": data['surname'], "имя": data['name']}
#results = db.child('codes').child(''.join(random.choices(string.ascii_uppercase + string.digits, k=8))).set(profile)
#print(results)
#добавление новых полей для ученика update()
# i1 = 0
# i1 += 1
# data = {"countAchievements": i1}
# results = db.child('users').child(user["localId"]).child("profile").update(data, user['idToken'])
# print(results)

#извлечение данных ученика с сервера
# student = db.child('users').child(user['localId']).child('profile').get()
# data = student.val()
# print(data["countAchievements"])
#создание хэша для реги
# profile = {"name": "name", "surname": "surname", "class": "8", "letter": "г", "email": "login",
#            "countAchievements": "0", "type": "user"}
#
# name_teacher = "я админ, мне можно"
# chars = '1234567890'
# for n in range(1):
#     password =''
#     for i in range(6):
#         password += random.choice(chars)
#     print(password)
# profile = {"name": name_teacher, "hash": password, "student": profile}
#
# db.child('hash').child(password).set(profile, user['idToken'])
# storage.child("ngRma2ISmdNzcWICuBd02EA4uRB2/-MPgSINwIKvyb6HfzLrI.jpg").download("C:\\games\\", "C:\\games\\3.jpg",
d = user['localId']  # upper token, profile token
achievements = db.child('users').child(user['localId']).child('achievements').get()
data = achievements.val()
for key in data:
    name = data[key]['competition_name']
    print(name)
    d = user['localId']
    upper_path = f'{d}/'
    file_name_base = f'{key}.{data[key]["file_format"]}'
    file_format = data[key]["file_format"]
    storage.child(f"{upper_path}{file_name_base}").download(f"C:/Users/кафношопа/Desktop/",
                                                            f"C:/Users/кафношопа/Desktop/d.docx",
                                                            token=user['idToken'])
    print(f"users/{upper_path}{file_name_base}")
    time.sleep(8)
#добавление достижения
# achievement = {"competition_type": "Хакатон", "competition_name": "Хакатон по ИИ", "work_type": "Решение задач",
#                "type_document": "Грамота", "date": "14.09.2020", "place": "Призер", "level_competition": "Региональный",
#                "subject": "Математика", "scan": "image/1.pdf"}
# results = db.child('users').child(user['localId']).child('achievements').push(achievement)
# print(results)

#извлечение данных достижения с сервера
# achievement = db.child('users').child(user['localId']).child('achievements').child("-MHfdxBeLRFMqd25siUA").get()
# data = achievement.val()
# print(data)
# print(data['level_competition'])

# извлечение данных всех достижений с сервера
# achievement = db.child('users').child(user['localId']).child('achievements').get()
# data = achievement.val()
# for key in data:
#     print(data[key]['competition_type'])

#загрузка и скачивание файлов
# storage.child("images/payment2.pdf").put("payment2.pdf", user['idToken'])
# storage.child("images2/payment2.pdf").download("payment3.pdf")

# storage.child("image3/img1.png").put("first_img.png", user['idToken'])
# storage.child("image3/img1.png").download("C:\\", "img4.png", user['idToken'])

# print(auth.get_account_info(user['idToken']))






