import paho.mqtt.client as mqtt
from gpiozero import *
import glob
import time
import os


ledG = LED(26)
ledSDB = LED(6)
ledS = LED(19)
ledC = LED(13)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
        
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("listen")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == "onG":
        ledG.on()
    if msg.payload == "offG":
        ledG.off()
    if msg.payload == "onSDB":
        ledSDB.on()
    if msg.payload == "offSDB":
        ledSDB.off()
    if msg.payload == "onS":
        ledS.on()
    if msg.payload == "offS":
        ledS.off()
    if msg.payload == "onC":
        ledC.on()
    if msg.payload == "offC":
        ledC.off()
    if msg.payload == "onA":
        ledG.on()
        ledSDB.on()
        ledS.on()
        ledC.on()
    if msg.payload == "offA":
        ledG.off()
        ledSDB.off()
        ledS.off()
        ledC.off()
    if msg.payload == "getTemp":
        print(read_temp())
        read_temp()
        return read_temp()
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Using the broker hosted at localhost
client.connect("localhost", 1883, 60)
# normally the IP section is filled with "localhost" or "127.0.0.1"
# this assumes that the MQTT broker is the Raspberry Pi itself
# this assumes that the MQTT broker service has already started
# check service status: sudo systemctl status mosquitto.service
client.loop_forever()
