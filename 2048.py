# -*- coding: utf-8 -*-
import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))

def main(stdscr):
    
    def init():
        '''initiate the board'''
        return 'Game'

    def not_game(state):
        '''展示游戏结束界面，判断重启还是结束'''
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        '''draw the board, read the action'''
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'

    state_actions = {'Init': init, 'Win':  lambda:not_game('Win'), 'Gameover':lambda: not_game('Gameover'),'Game': game}
    state = 'Init'
    while state != 'Exit':
        state = state_actions[state]()

def det_user_action(keyboard):
    char = 'N'
    while char not in action_dict:
        char = keyboard.getch()
    return actions_dict[char]

class GameField(object):
    def __init_--(self, height=4, width=4, win-2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j]
                                      
        
