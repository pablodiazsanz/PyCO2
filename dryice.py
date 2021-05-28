import time
import board
import adafruit_scd30
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

i2c = board.I2C()   # uses board.SCL and board.SDA
scd = adafruit_scd30.SCD30(i2c)

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if scd.data_available:
        print("Data Available!")
        print("CO2:", scd.CO2, "PPM")
        print("Temperature:", scd.temperature, "degrees C")
        print("Humidity:", scd.relative_humidity, "%%rH")
        print("")
        print("Waiting for new data...")
        print("")
        data = {"CO2 (ppm)": scd.CO2, "Temperatura (grados C)": scd.temperature, "Humedad relativa (porcentaje)": scd.relative_humidity}
        db.push(data)

    time.sleep(2.5)
