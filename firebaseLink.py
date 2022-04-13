# pip install firebase_admin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

# Firebase database 인증 및 앱 초기화
db_url = 'https://lms-assignment-default-rtdb.firebaseio.com/'

cred = credentials.Certificate("lms-assignment-firebase-adminsdk-gg9hv-0e2b022f8b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : db_url
})
# 학번이 있는지 확인, 이후 db.reference('학번') 으로 JSON Response
ref = db.reference('20171473')
print(ref.get())