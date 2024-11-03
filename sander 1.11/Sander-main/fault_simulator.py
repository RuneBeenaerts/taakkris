

def faultSimulator(client,team, player):

    client.loop_start()
    message = f"Fault by {player} from {team}!"
    client.publish("football/match/events/fault", message)
    print(f"Published Fault: {message}")
    client.loop_stop()
