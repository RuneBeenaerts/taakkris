

def simulateExtraTime(client,time):
    client.loop_start()
    message = f"Extra time:  +{time}  "
    client.publish('football/match/events/extraTime', message)
    print(f"Extra time:  +{time}")
    client.loop_stop()