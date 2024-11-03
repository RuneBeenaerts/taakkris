
def publish_goal(client, team, player, assistent):
    client.loop_start()
    message = f"Goal by {player} from {team} assisted by {assistent}!"
    client.publish("football/match/events/goal", message)
    print(f"Published goal: {message}")
    client.loop_stop()

