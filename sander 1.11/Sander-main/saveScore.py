import json

def get_scores(filename="scores.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Barcelona": 0, "Bayern Munich": 0}  # Standaard scores

def save_score(scores, filename="scores.json"):
    with open(filename, "w") as file:
        json.dump(scores, file)

def reset_scores(filename="scores.json"):
    reset_score = {
        "Barcelona": 0,
        "Bayern Munich": 0
    }
    save_score(reset_score, filename)
