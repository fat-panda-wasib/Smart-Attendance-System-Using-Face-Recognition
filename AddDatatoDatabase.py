import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-system-aada2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "191902034":
        {
            "name": "Ahsanul Karim",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902056":
        {
            "name": "Md. Ariful Islam",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902025":
        {
            "name": "Kazi Hasnayeen Emad",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902012":
        {
            "name": "Md. Abu Bakar Siddik",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902017":
        {
            "name": "Santo Ahmed",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902029":
        {
            "name": "Jahidul Islam",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902057":
        {
            "name": "Minhazul Islam",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
    "191902065":
        {
            "name": "Tanvir Haider",
            "department": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-06 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)