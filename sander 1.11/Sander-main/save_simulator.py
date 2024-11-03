

def simulateSave(client,keeper):
    client.loop_start()
    message = f"Save by {keeper}"
    client.publish("football/match/events/save", message)
    print( f"Published Save: {message}")
    client.loop_stop()