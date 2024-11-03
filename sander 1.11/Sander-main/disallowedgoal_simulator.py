

def simulateDisallowedGoal(client,team, player):
    client.loop_start()
    message = f'Disallowed goal for {team} from {player}'
    client.publish('football/match/events/disallowedGoal', message)
    print(f"Disallowed goal for {team} from {player}")
    client.loop_stop()
