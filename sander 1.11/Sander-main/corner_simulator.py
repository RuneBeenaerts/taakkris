

def simulateCorner(client,team):
    client.loop_start()
    message = f"Corner for {team} !"
    client.publish("football/match/events/corner", message)
    print(f"Published corner: {message}")
    client.loop_stop()