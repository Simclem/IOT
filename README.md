This Project is a school project in IOT course.

All GPIOS are in MQTT.py

We have a three parts on this app : 

- MQTT's message broker which gives order to different components
- We have a python flask server which gives order to mqtt
- A front angular part which send orders to python flask with an IHM

First of all you have to replace all ip addresses by Raspberry IP (They are all in app.component.ts, and app.service.ts)

To run it you have to clone the project, and launch : 

python mqtt.py at the root
python manage.py at the root
and npm i then npm run when you are in /front/FrontIOT



Now open you web browser and search localhost:4200.

The apps is running.

