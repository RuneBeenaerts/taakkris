import time
from time_simulator import publish_time
from goal_simulator import publish_goal
from fault_simulator import faultSimulator
from corner_simulator import simulateCorner
from save_simulator import simulateSave
from offside_simulator import simulateOffside
from disallowedgoal_simulator import simulateDisallowedGoal
from shot_simulator import simulateShot
from freekick_simulator import simulateFreekick
from card_simulator import simulateCard
from substitute_simulator import simulateSubstitute
from time_simulator import publish_extra_time
from time_simulator import extra_time_exceeded_first
from time_simulator import extra_time_exceeded_second
from saveScore import save_score, get_scores, reset_scores  # Importeer de juiste functies
import paho.mqtt.client as mqtt

mqttBroker = "fcbe9d6b471d4f2fbf6f6d269817368e.s1.eu.hivemq.cloud"
client = mqtt.Client("match_publisher")
client.username_pw_set("Sander", "ScHc?!2004")
client.tls_set()
client.connect(mqttBroker, 8883)

reset_scores() #reset de score

# Initialisatie
time_passed = 0
extra_time_first_half = 3  # Stel extra tijd in voor de eerste helft
extra_time_second_half = 3  # Stel extra tijd in voor de tweede helft
extra_time_second_half_setter = 3
in_extra_time = False  # Indicator voor extra tijd
scores = get_scores()  # Laad de scores bij het starten van de simulator

if __name__ == '__main__':
    while time_passed < (90 + extra_time_second_half_setter):
        time.sleep(1)

        # Controleer of we in de eerste of tweede helft zijn voor extra tijd
        if time_passed >= 45 and extra_time_first_half > 0:
            in_extra_time = True
            if time_passed == 45:
                publish_extra_time(client, f"extra time: 45+{extra_time_first_half}")

            time_passed += 1
            extra_time_first_half -= 1
            publish_time(client, f"in extra time: {time_passed}")
            if time_passed == 48:
                simulateCorner(client, 'Barcelona')
            if extra_time_first_half == 0:  # Reset na extra tijd in de eerste helft
                extra_time_exceeded_first(client)
                time_passed = 45
                in_extra_time = False
            continue

        elif time_passed >= 90 and extra_time_second_half > 0:
            in_extra_time = True
            if time_passed == 90:
                publish_extra_time(client, f"extra time: 90+{extra_time_second_half}")

            time_passed += 1
            extra_time_second_half -= 1
            publish_time(client, f"in extra time: {time_passed}")
            if time_passed == 93:
                faultSimulator(client, 'Bayern Munich', 'Coman')
            if extra_time_second_half == 0:  # Reset na extra tijd in de tweede helft
                extra_time_exceeded_second(client)
            continue

        # Verhoog normale speeltijd als we niet in extra tijd zijn
        if not in_extra_time:
            time_passed += 1
            publish_time(client, time_passed)

        # Logica voor doelpunten en andere gebeurtenissen
        if time_passed == 1:
            scores['Barcelona'] += 1
            publish_goal(client, "Barcelona", 'Raphinha', 'Lopez')
            save_score(scores)  # Sla de score op

        if time_passed == 5:
            faultSimulator(client, 'Bayern Munich', 'Upamecano')
        if time_passed == 8:
            simulateCorner(client, 'Bayern Munich')
        if time_passed == 8:
            simulateCorner(client, 'Kane')
        if time_passed == 8:
            simulateSave(client, 'Pena')
        if time_passed == 10:
            simulateOffside(client, 'Kane')
        if time_passed == 11:
            simulateDisallowedGoal(client, 'Bayern Munich', 'Kane')
        if time_passed == 13:
            simulateOffside(client, 'Gnabry')
        if time_passed == 13:
            faultSimulator(client, 'Bayern Munich', 'Kim Min Jae')
        if time_passed == 16:
            simulateShot(client, 'Kane')
        if time_passed == 17:
            simulateShot(client, 'Gnabry')
        if time_passed == 16:
            simulateSave(client, 'Pena')
        if time_passed == 18:
            scores['Bayern Munich'] += 1
            publish_goal(client, 'Bayern Munich', 'Kane', 'Gnabry')
            save_score(scores)  # Sla de score op

        if time_passed == 20:
            faultSimulator(client, 'Bayern Munich', 'Upamecano')
        if time_passed == 21:
            faultSimulator(client, 'Bayern Munich', 'Palhinha')
        if time_passed == 23:
            simulateShot(client, 'Olise')
        if time_passed == 24:
            simulateFreekick(client, 'Barcelona')
        if time_passed == 26:
            simulateShot(client, 'Lewandowski')
        if time_passed == 27:
            faultSimulator(client, 'Bayern Munich', 'Kimmich')
        if time_passed == 27:
            simulateCard(client, 'Kimmich', 'yellow')
        if time_passed == 29:
            simulateCorner(client, 'Barcelona')
        if time_passed == 30:
            faultSimulator(client, 'Barcelona', 'Lopez')
        if time_passed == 32:
            faultSimulator(client, 'Barcelona', 'Lewandowski')
        if time_passed == 34:
            faultSimulator(client, 'Barcelona', 'Lewandowski')
        if time_passed == 36:
            scores['Barcelona'] += 1
            publish_goal(client, "Barcelona", 'Lewandowski', 'Lopez')
            save_score(scores)  # Sla de score op
        if time_passed == 38:
            faultSimulator(client, 'Barcelona', 'Yamal')
        if time_passed == 40:
            faultSimulator(client, 'Barcelona', 'Balde')
        if time_passed == 45:
            scores['Barcelona'] += 1
            publish_goal(client, "Barcelona", 'Raphinha', 'Casado')
            save_score(scores)  # Sla de score op
        if time_passed == 48:
            faultSimulator(client, 'Barcelona', 'Koundé')
        if time_passed == 48:
            faultSimulator(client, 'Barcelona', 'Casado')
        if time_passed == 50:
            simulateShot(client, 'Olise')
        if time_passed == 51:
            simulateShot(client, 'Palhinha')
        if time_passed == 53:
            simulateOffside(client, 'Gnabry')
        if time_passed == 55:
            faultSimulator(client, 'Barcelona', 'Casado')
        if time_passed == 56:
            scores['Barcelona'] += 1
            publish_goal(client, "Barcelona", 'Raphinha', 'Yamal')
            save_score(scores)  # Sla de score op
        if time_passed == 58:
            simulateShot(client, 'Kimmich')
        if time_passed == 60:
            simulateSubstitute(client, 'Bayern Munich', 'Olise', 'Sané')
        if time_passed == 60:
            simulateSubstitute(client, 'Bayern Munich', 'Müller', 'Musiala')
        if time_passed == 60:
            simulateSubstitute(client, 'Bayern Munich', 'Gnabry', 'Coman')
        if time_passed == 60:
            simulateSubstitute(client, 'Bayern Munich', 'Palhinha', 'Goretzka')
        if time_passed == 60:
            simulateCorner(client, 'Bayern Munich')
        if time_passed == 61:
            faultSimulator(client, 'Bayern Munich', 'Coman')
        if time_passed == 61:
            simulateSubstitute(client, 'Barcelona', 'Lopez', 'De Jong')
        if time_passed == 62:
            simulateShot(client, 'Balde')
        if time_passed == 62:
            simulateCorner(client, 'Barcelona')
        if time_passed == 63:
            simulateOffside(client, 'Yamal')
        if time_passed == 64:
            faultSimulator(client, 'Barcelona', 'De Jong')
        if time_passed == 65:
            faultSimulator(client, 'Bayern Munich', 'Sané')
        if time_passed == 66:
            simulateShot(client, 'Coman')
        if time_passed ==67:
            faultSimulator(client,'Bayern Munich','Kim Min Jae')
        if time_passed==72:
            simulateShot(client, 'Musiala')
        if time_passed==73:
            simulateCorner(client, 'Bayern Munich')
        if time_passed==74:
            simulateCorner(client, 'Bayern Munich')
        if time_passed==76:
            simulateSubstitute(client, 'Barcelona', 'Raphinha','Olmo')
        if time_passed ==78:
            simulateShot(client,'Yamal')
        if time_passed == 78:
            simulateCorner(client, 'Barcelona')
        if time_passed == 80:
            simulateCorner(client, 'Barcelona')
        if time_passed==80:
            simulateShot(client,'Cubarsi')
        if time_passed == 80:
            simulateShot(client, 'De Jong')
        if time_passed == 80:
            simulateShot(client, 'Lewandowski')
        if time_passed == 80:
            simulateShot(client, 'De Jong')
        if time_passed==81:
            faultSimulator(client,'Barcelona','Cubarsi')
        if time_passed == 82:
            faultSimulator(client, 'Barcelona', 'Koundé')
        if time_passed == 85:
            simulateSubstitute(client, 'Barcelona', 'Pedri', 'Gavi')
        if time_passed == 85:
            simulateSubstitute(client, 'Barcelona', 'Yamal', 'Fati')
        if time_passed == 85:
            simulateSubstitute(client, 'Barcelona', 'Lewandowksi', 'Viktor')
        if time_passed == 86:
            simulateSubstitute(client, 'Bayern Munich', 'Guerreiro', 'Laimer')
        if time_passed==88:
            simulateCorner(client,'Bayern Munich')
        if time_passed==89:
            simulateShot(client, 'Musiala')
        if time_passed==90:
            simulateCard(client,'Goretzka','Yellow')