

def simulateOffside(client,player):
    client.loop_start()
    message = f"offside by {player}"
    client.publish("football/match/events/offside", message)
    print(f"Published offside: {message}")
    client.loop_stop()
