import sys, pygame
from pygame.locals import *

white = 255,255,255
blue = 202,225,255
pink = 255,192,203
myfont = pygame.font.Font(None, 30)


class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        f = open("QA.txt", "r")
        trivia_data = f.readlines()
        f.close()

        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1

    def show_question(self):
        print_text(myfont, 210, 5, "TRIVIA GAME", white)
        print_text(myfont, 190, 500-20, "Press Keys (1-4) To Answer", white)
        print_text
