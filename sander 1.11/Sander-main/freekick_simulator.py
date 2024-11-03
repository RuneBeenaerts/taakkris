
def simulateFreekick(client,team):
    client.loop_start()
    message = f"Freekick for {team} "
    client.publish('football/match/events/freekick', message)
    print(f"Freekick for {team}")
    client.loop_stop()