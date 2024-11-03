


def simulateShot(client,player):
    client.loop_start()
    message = f"Shot by {player}"
    client.publish("football/match/events/shot", message)
    print(f"Published corner: {message}")
    client.loop_stop()