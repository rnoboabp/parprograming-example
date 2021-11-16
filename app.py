""""""
import random

player_1 = "0"
player_2 = "0"

POINTS = ["0", "15", "30", "40", "40+1", "40+2"]

PLAYER_RESULT_A = "PayerOne 0 PlayerTwo 0"
PLAYER_RESULT_B = "PayerOne 30 PlayerTwo 15"
PLAYER_RESULT_C = "Deuce"
PLAYER_RESULT_D = "Advantage PlayerOne"
PLAYER_RESULT_E = "Advantage PlayerTwo"
PLAYER_RESULT_F = "PlayerTwo Wins"


def turn_players():
    yield POINTS[0]
    yield POINTS[1]
    yield POINTS[2]
    yield POINTS[3]
    yield POINTS[4]
    yield POINTS[5]


def result_player(p1, p2):
    """

    :return:
    """
    if p1 == "0" and p2 == "0":
        return PLAYER_RESULT_A
    elif p1 == "30" and p2 == "15":
        return PLAYER_RESULT_B
    elif p1 == "40" and p2 == "40":
        return PLAYER_RESULT_C


# player_1 = turn_players()
# print(next(player_1))
# print(next(player_1))

while True:
    print("----- Starting player -----")
    counter = 0
    player_1 = turn_players()
    player_2 = turn_players()
    counter += 1
