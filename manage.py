from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"



@app.route('/allLightsOn')
def allLightsOn():
    return "allLightsOn"

@app.route('/allLightsOff')
def allLightsOff():
    return "allLightsOff"

@app.route('/getTemperature')
def getTemperature():
    return "getTemperature"

if __name__ == '__main__':
    app.run()