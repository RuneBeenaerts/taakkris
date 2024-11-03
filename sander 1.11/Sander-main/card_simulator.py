import paho.mqtt.client as mqtt

def simulateCard(client,player,color):
    message = f"{color} card for {player} "
    client.publish('football/match/events/card', message)
    print(f"{color} card for {player}")
