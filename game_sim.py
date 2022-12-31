import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets
import player_editor
import batting_order
import random

player_list = player_editor.load_list("c:\\Ib project\\player_editor.db")
batting_list = batting_order.load_list("c:\\Ib project\\BattingOrder.pickle")

def half_inning(batting_order, lead_off):
    outs = 0
    total_bases = plate_app(player_list[batting_order[lead_off]])
    if total_bases == 0:
        outs += 1
    if outs == 3:
        pass
def plate_app(batter):
    total_bases = 0
    outcome = random.randint(1, batter["PA"])
    if outcome <= batter["B1"]:
        total_bases = 1
    elif outcome <= batter["B1"] + batter["B2"]:
        total_bases = 2
    elif outcome <= batter["B1"] + batter["B2"] + batter["B3"]:
        total_bases = 3
    elif outcome <= batter["B1"] + batter["B2"] + batter["B3"] + batter["B4"]:
        total_bases = 4
    elif outcome <= batter["B1"] + batter["B2"] + batter["B3"] + batter["B4"] + batter["BB"]:
        total_bases = 1
    elif outcome <= batter["B1"] + batter["B2"] + batter["B3"] + batter["B4"] + batter["BB"] + batter["HBP"]:
        total_bases = 1
    elif outcome <= batter["B1"] + batter["B2"] + batter["B3"] + batter["B4"] + batter["BB"] + batter["HBP"] + batter["SO"]:
        total_bases = 0
    else: ## in play and out
        total_bases = 0
    return total_bases

def pitch():
    """" here if I add pitching and defense """
    pass
def game():
    inning = 1
    score_home_total = 0
    score_computer_total = 0
    score_computer_inning = half_inning()
    inning += .5
    score_home_inning = half_inning()
    inning += .5
    if inning >=9.5 and score_home_total > score_computer_total:
        pass
    else:
        pass
    if inning >=10 and score_home_total < score_computer_total:
        pass

if __name__ == "__main__":
    half_inning(batting_list, 0)
