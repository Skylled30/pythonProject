import pyrebase

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