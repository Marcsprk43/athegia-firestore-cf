import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pandas import Series
import datetime

import os

# Use the application default credentials
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred, {
  'projectId': 'athegiamedical',
})

db = firestore.client()


