import numpy
import os

opponent_rock = "A"
opponent_paper = "B"
opponent_scissors = "C"

me_rock = "X"
me_paper = "Y"
me_scissors = "Z"

strategy_lose = "X"
strategy_draw = "Y"
strategy_win = "Z"

def score_for_the_play(my_play):
    score = 0
    if my_play == me_rock:
            score = 1
    elif my_play == me_paper:
            score =  2
    elif my_play == me_scissors:
            score = 3
    else:
        print("Uhh, scoring didn't find a match of what was currently played")
    # print("I played", my_play, "Which scored", score)
    return score

def score_for_the_match(my_play, opponents_play):
    if my_play == me_rock:
        if opponents_play == opponent_scissors:
            return 6
        elif opponents_play == opponent_rock:
            return 3
        elif opponents_play == opponent_paper:
            return 0
        else:
            print("I played", my_play, "can't process what the opponent played ==>", opponents_play)

    if my_play == me_paper:
        if opponents_play == opponent_rock:
            return 6
        elif opponents_play == opponent_paper:
            return 3
        elif opponents_play == opponent_scissors:
            return 0
        else:
            print("I played", my_play, "can't process what the opponent played ==>", opponents_play)

    if my_play == me_scissors:
        if opponents_play == opponent_paper:
            return 6
        elif opponents_play == opponent_scissors:
            return 3
        elif opponents_play == opponent_rock:
            return 0
        else:
            print("I played", my_play, "can't process what the opponent played ==>", opponents_play)

def what_move_to_loose(opponents_move):
    suggested_move = ""
    if opponents_move == opponent_rock:
        suggested_move = me_scissors
    elif opponents_move == opponent_paper:
        suggested_move = me_rock
    elif opponents_move == opponent_scissors:
        suggested_move = me_paper
    return suggested_move

def what_move_to_win(opponents_move):
    suggested_move = ""
    if opponents_move == opponent_rock:
        suggested_move = me_paper
    elif opponents_move == opponent_paper:
        suggested_move = me_scissors
    elif opponents_move == opponent_scissors:
        suggested_move = me_rock
    return suggested_move

def what_move_to_draw(opponents_move):
    suggested_move = ""
    if opponents_move == opponent_rock:
        suggested_move = me_rock
    elif opponents_move == opponent_paper:
        suggested_move = me_paper
    elif opponents_move == opponent_scissors:
        suggested_move = me_scissors
    return suggested_move

def what_should_i_play(opponents_play, strategy):
    my_play = ""
    if strategy == strategy_lose:
        my_play = what_move_to_loose(opponents_play)
    elif strategy == strategy_win:
        my_play = what_move_to_win(opponents_play)
    elif strategy == strategy_draw:
        my_play = what_move_to_draw(opponents_play)
    return my_play

# print("current working directory", os.getcwd())
strategy_file_name = 'data/data1'
strategy_file = open(strategy_file_name, 'r')
strategy_array = numpy.genfromtxt(strategy_file, delimiter=" ", dtype="str")

scores = []
for play in strategy_array:
    opponents_play = play[0]
    my_strategy = play[1]
    my_play = what_should_i_play(opponents_play, my_strategy)
    # print("My Play", score_for_the_play(my_play))
    # print("The Score", score_for_the_match(my_play, opponents_play))
    score = int(score_for_the_play(my_play)) + int(score_for_the_match(my_play, opponents_play))
    scores.append(score)

print("Total score", numpy.sum(scores))