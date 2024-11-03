import paho.mqtt.client as mqtt

# Deze functie wordt aangeroepen wanneer de client verbinding maakt met de broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Abonneer op de onderwerpen voor het ontvangen van berichten
    client.subscribe("football/match/time")
    client.subscribe("football/match/events/card")
    client.subscribe("football/match/events/corner")
    client.subscribe("football/match/events/fault")
    client.subscribe("football/match/events/goal")
    client.subscribe("football/match/events/extraTime")
    client.subscribe("football/match/events/freekick")
    client.subscribe("football/match/events/disallowedGoal")
    client.subscribe("football/match/events/offside")
    client.subscribe("football/match/events/save")
    client.subscribe("football/match/events/shot")
    client.subscribe("football/match/events/substitute")
# Deze functie wordt aangeroepen wanneer een bericht wordt ontvangen
def on_message(client, userdata, messages):
    # Decodeer het bericht en print het
    print(f"Received message on topic {messages.topic}: {messages.payload.decode('utf-8')}")

mqttBroker = "fcbe9d6b471d4f2fbf6f6d269817368e.s1.eu.hivemq.cloud"
client = mqtt.Client("Smartphone")  # Een unieke naam voor deze client
client.username_pw_set("Sander", "ScHc?!2004")  # Voeg hier je gebruikersnaam en wachtwoord toe
client.tls_set()  # Beveiligde verbinding
client.connect(mqttBroker, 8883)  # Maak verbinding met de broker

# Koppel de callback functies
client.on_connect = on_connect
client.on_message = on_message

client.loop_start()  # Start de loop

try:
    # Houd de subscriber actief voor 30 seconden
    print("Subscriber is listening for messages...")
    while True:
        pass  # Laat de loop blijven draaien

except KeyboardInterrupt:
    print("Subscriber stopped.")
finally:
    client.loop_stop()  # Stop de loop
    client.disconnect()  # Verbreek de verbinding
