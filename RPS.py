import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    n = 3
    guess = "R"

    if len(opponent_history) > n:
        seq = "".join(opponent_history[-n:])
        if "memory" not in player.__dict__:
            player.memory = {}
        if seq not in player.memory:
            player.memory[seq] = {"R": 0, "P": 0, "S": 0}

        prev_seq = "".join(opponent_history[-n-1:-1])
        if prev_seq in player.memory:
            player.memory[prev_seq][opponent_history[-1]] += 1

        options = player.memory.get(seq, {"R": 0, "P": 0, "S": 0})
        prediction = max(options, key=options.get)

        if prediction == "R":
            guess = "P"
        elif prediction == "P":
            guess = "S"
        else:
            guess = "R"
    else:
        guess = random.choice(["R", "P", "S"])

    return guess
