import pyrebase

firebaseConfig = {
    "apiKey" : "AIzaSyBOGKPuzQv8Ocik-fDBnyFniU3sDBvw5Ls",
    "authDomain" : "dryicepfc.firebaseapp.com",
    "projectId" : "dryicepfc",
    "databaseURL": "https://dryicepfc-default-rtdb.firebaseio.com/",
    "storageBucket" : "dryicepfc.appspot.com",
    "messagingSenderId" : "70730620689",
    "appId" : "1:70730620689:web:8d1b9154541ad93f9936b0"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data = {"marca" : "Porsche", "modelo" : 911, "Potencia" : "420cv"}

db.push(data)

