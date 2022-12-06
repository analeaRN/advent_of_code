"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""
import general as g
strategy = g.read_file("./2022/input.txt")

rock = "A"
paper = "B"
scissors = "C"

SCORES = {
    "LOSE": 0,
    "WIN": 6,
    "DRAW": 3,
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3  # Scissors
}


def decrypt_play(encrypted_play: str):
    """used in part 1"""
    if encrypted_play == "X":
        return rock
    elif encrypted_play == "Y":
        return paper
    elif encrypted_play == "Z":
        return scissors
    else: 
        return encrypted_play

def get_play(player_move: str, opponent_move: str):
    if player_move == "X":
        return get_loss(opponent_move)
    elif player_move == "Z":
        return get_win(opponent_move)
    else: 
        return opponent_move


def get_win(move: str):
    if move == rock:
        return paper
    elif move == paper:
        return scissors
    elif move == scissors:
        return rock

def get_loss(move: str):
    if move == rock:
        return scissors
    elif move == paper:
        return rock
    elif move == scissors:
        return paper


def get_draw(move: str):
    return move  # lol

def check_win(opponents_move: str, your_move: str):
    if your_move == opponents_move:
        return SCORES.get("DRAW")
    elif your_move == rock:
        if opponents_move == paper:
            return SCORES.get("LOSE")
        else:
            return SCORES.get("WIN")
    elif your_move == paper:
        if opponents_move == scissors:
            return SCORES.get("LOSE")
        else:
            return SCORES.get("WIN")
    elif your_move == scissors:
        if opponents_move == rock:
            return SCORES.get("LOSE")
        else:
            return SCORES.get("WIN")


def win(opponent: str, your_move: str):
    return get_win(opponent, decrypt_play(your_move))

def part_1():
    score = 0
    for play in strategy.splitlines():
        # print(play)
        opponent, player = play.split()
        decrypted_play = decrypt_play(player)
        win_state = check_win(opponent, decrypted_play)
        # print(opponent, player, decrypted_play, win_state)
        score += (win_state + SCORES.get(decrypted_play))
        
    print("final score is", score)
    return score


def part_2():
    score = 0    
    for play in strategy.splitlines():
        # print(play)
        opponent, desired_win_state = play.split()
        
        player_move = get_play(desired_win_state, opponent)
        win_state = check_win(opponent, player_move)

        # print(opponent, player_move, desired_win_state, win_state, "::", win_state + SCORES.get(player_move))
        score += (win_state + SCORES.get(player_move))

    print("final score is", score)
    return score


def main():
    g.print_parts(part_1(), part_2())


main()
