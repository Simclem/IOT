from flask import Flask
from flask_cors import CORS
import os
import time

ledG = False
ledSDB = False
ledS = False
ledC = False
os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offA")  

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello World!"



@app.route('/getStatus')
def getStatus():
    global ledG
    global ledSDB
    global ledS
    global ledC

    return "{\"data\":[{\"G\": \""+str(ledG)+"\"},{\"SDB\": \""+str(ledSDB)+"\"},{\"S\": \""+str(ledS)+"\"},{\"C\": \""+str(ledC)+"\"}]}"


@app.route('/ALightOn')
def AllLightsOn():
    global ledG
    global ledSDB
    global ledS
    global ledC
    
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onA")
    ledG = True
    ledSDB = True
    ledS = True
    ledC = True
    return ""

@app.route('/ALightOff')
def AllLightsOff():
    global ledG
    global ledSDB
    global ledS
    global ledC
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offA")  
    ledG = False
    ledSDB = False
    ledS = False
    ledC = False
    return ""


@app.route('/GLightSwitch')
def GSwitch():
    global ledG

    if ledG == True : 
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offG")
        ledG = False
    else :
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onG")
        ledG = True
    return "{\"status\" : \""+str(ledG)+"\"}"

@app.route('/GLightOn')
def GLightsOn():
    global ledG

    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onG")
    ledG = True
    return ""

@app.route('/GLightOff')
def GLightsOff():
    global ledG
    ledG = False
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offG")
    return ""

@app.route('/SLightSwitch')
def SSwitch():
    global ledS

    if ledS == True : 
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offS")
        ledS = False
    else :
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onS")
        ledS = True
    return "{\"status\" : \""+str(ledS)+"\"}"
@app.route('/SLightOn')
def SLightsOn():
    global ledS
    ledS = True
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onS")
    return ""

@app.route('/SLightOff')
def SLightsOff():
    global ledS
    ledS = False
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offS")
    return ""

@app.route('/SDBLightSwitch')
def SDBSwitch():
    global ledSDB
    if ledSDB == True : 
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offSDB")
        ledSDB = False
    else :
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onSDB")
        ledSDB = True
    return "{\"status\" : \""+str(ledSDB)+"\"}"

@app.route('/SDBLightOn')
def SDBLightsOn():
    global ledSDB
    ledSDB = True
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onSDB")
    return ""

@app.route('/SDBLightOff')
def SDBLightsOff():
    global ledSDB
    ledSDB = False
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offSDB")
    return ""

@app.route('/CLightSwitch')
def CSwitch():
    global ledC
    if ledC == True : 
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offC")
        ledC = False
    else :
        os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onC")
        ledC = True
    return "{\"status\" : \""+str(ledC)+"\"}"

@app.route('/CLightOn')
def CLightsOn():
    global ledC
    ledC = True
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m onC")
    return ""

@app.route('/CLightOff')
def CLightsOff():
    global ledC
    ledC = False
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m offC")
    return ""

@app.route('/GetTemp')
def GetTemp():
    os.system("mosquitto_pub -h 127.0.0.1 -t listen -m getTemp")
    time.sleep(3)
    f= open("./temp.txt","r")
    data = f.readlines()
    f.close()
    return str(data[0])
    #return ''



if __name__ == '__main__':
    app.run(host= '0.0.0.0')
