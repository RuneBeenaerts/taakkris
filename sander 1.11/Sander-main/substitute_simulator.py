
def simulateSubstitute(client,team,player1,player2):
    client.loop_start()
    message = f"Substitute for {team}, {player1} out and {player2} in"
    client.publish('football/match/events/substitute', message)
    print(f' Substitute for {team}, {player1} out and {player2} in')
    client.loop_stop()