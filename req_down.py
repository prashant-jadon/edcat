import requests
import pyrebase
import requests

config = {
    "apiKey" : "AIzaSyAetMmzyqpksGjdvXbYVAk5gWmEdH4GC1I",
    "authDomain" : "unseen1-1.firebaseapp.com",
    "databaseURL" : "https://unseen1-1-default-rtdb.firebaseio.com",
    "projectId" : "unseen1-1",
    "storageBucket" : "unseen1-1.appspot.com",
    "messagingSenderId" : "336843569987",
    "appId" : "1:336843569987:web:76be1bbee6a4e8098a8df6",
    "measurementId" : "G-REW7MW4FZB",
    "serviceAccount": "service_acc.json"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
files = storage.list_files()


for file in files:
    nameofthefile = file.name
    z = storage.child(file.name).get_url(None)
    print(z)

