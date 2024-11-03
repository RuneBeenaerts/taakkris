
def publish_time(client,time_elapsed):
    client.loop_start()
    client.publish("football/match/time", f"{time_elapsed}'")
    print(f"Published time: {time_elapsed}'")
    client.loop_stop()

def publish_extra_time(client,time_elapsed):
    client.loop_start()
    client.publish("football/match/time", f"{time_elapsed}")
    print(f"Published time: {time_elapsed}")
    client.loop_stop()
def extra_time_exceeded_first(client):
    client.loop_start()
    client.publish("football/match/time", f"end first half")
    print(f"Published time: end first half")
    client.loop_stop()
def extra_time_exceeded_second(client):
    client.loop_start()
    client.publish("football/match/time", f"end second half")
    print(f"Published time: end second half")
    client.loop_stop()