from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"





@app.route('/ALightOn')
def AllLightsOn():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onA")
    return ""

@app.route('/ALightOff')
def AllLightsOff():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offA")
    return ""



@app.route('/GLightOn')
def GLightsOn():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onG")
    return ""

@app.route('/GLightOff')
def GLightsOff():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offG")
    return ""

@app.route('/SLightOn')
def SLightsOn():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onS")
    return ""

@app.route('/SLightOff')
def SLightsOff():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offS")
    return ""

@app.route('/SDBLightOn')
def SDBLightsOn():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onSDB")
    return ""

@app.route('/SDBLightOff')
def SDBLightsOff():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offSDB")
    return ""


@app.route('/CLightOn')
def CLightsOn():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onC")
    return ""

@app.route('/CLightOff')
def CLightsOff():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offC")
    return ""

@app.route('/GetTemp')
def GetTemp():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m getTemp")
    return ""



if __name__ == '__main__':
    app.run()