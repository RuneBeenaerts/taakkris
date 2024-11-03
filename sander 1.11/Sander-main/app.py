from flask import Flask, render_template, jsonify
from paho.mqtt import client as mqtt_client
from saveScore import get_scores, save_score
import time

app = Flask(__name__)

# MQTT settings
mqttBroker = "fcbe9d6b471d4f2fbf6f6d269817368e.s1.eu.hivemq.cloud"
mqttPort = 8883
mqttUser = "Sander"
mqttPassword = "ScHc?!2004"
topic = "football/match/#"

events = []
time_info = ""


# Callback for when a message is received
def on_message(client, userdata, message):
    global events, time_info
    msg = message.payload.decode()

    # Update time_info if the message is about time
    if message.topic == "football/match/time":
        time_info = msg  # Stel time_info in op het ontvangen bericht
    else:
        # Voor elk ontvangen bericht, voeg het toe aan de events lijst
        events.append(f"{msg}")  # Toevoegen aan de events-lijst


# Connect and subscribe to the MQTT broker
def connect_mqtt():
    client = mqtt_client.Client()
    client.username_pw_set(mqttUser, mqttPassword)
    client.tls_set()
    client.connect(mqttBroker, mqttPort)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_start()
    return client


mqtt_client = connect_mqtt()


@app.route('/')
def index():
    return render_template('index.html', events=events, time_info=time_info)


@app.route('/data')
def data():
    return jsonify(time_info=time_info, events=events)


@app.route('/score')
def get_score():
    scores = get_scores()  # Haal huidige score op uit scores.json
    return jsonify({
        "Barcelona": scores.get("Barcelona", 0),  # Directe score zonder geneste dict
        "Bayern Munich": scores.get("Bayern Munich", 0)
    })


@app.route('/events')
def get_events():
    return jsonify(events)  # Retourneer de huidige evenementenlijst als JSON


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
