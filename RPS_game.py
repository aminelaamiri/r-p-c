import random

def play(player1, player2, num_games, verbose=False):
    p1 = ""
    p2 = ""
    p1_score = 0
    p2_score = 0
    for i in range(num_games):
        p1 = player1(p2)
        p2 = player2(p1)
        if verbose:
            print("Game", i, ":", p1, "vs", p2)
        if p1 == p2:
            continue
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            p1_score += 1
        else:
            p2_score += 1
    if verbose:
        print("Final Score:", p1_score, "to", p2_score)
    return p1_score / num_games

# --- Bots adversaires ---

def quincy(prev_play, opponent_history=[]):
    # Quincy suit un cycle fixe
    options = ["R", "P", "S", "R", "P"]
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    return options[len(opponent_history) % len(options)]

def abbey(prev_play, opponent_history=[]):
    # Abbey essaie de prédire ton prochain coup
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]
    return guess

def kris(prev_play, opponent_history=[]):
    # Kris joue toujours le coup qui bat ton dernier
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    if prev_play == "":
        return "R"
    if prev_play == "R":
        return "P"
    if prev_play == "P":
        return "S"
    if prev_play == "S":
        return "R"

def mrugesh(prev_play, opponent_history=[]):
    # Mrugesh joue en fonction de la fréquence de tes coups
    if prev_play == "":
        opponent_history.clear()
    opponent_history.append(prev_play)
    if not opponent_history:
        return "R"
    most_common = max(set(opponent_history), key=opponent_history.count)
    if most_common == "R":
        return "P"
    if most_common == "P":
        return "S"
    return "R"
