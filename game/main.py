from .board import BOARD
from .ai import COMP
import pygame

pygame.init()


class GAME:
    def __init__(self):
        self.board = BOARD()
        self.ai = COMP()
        self.run = False

    def update(self, surface):
        self.draw(surface)
        self.ai_turn()

    def draw(self, surface):
        if not self.run:
            self.board.draw_menu(surface)
            return
        self.board.draw_board(surface)
        if self.board.is_ended():
            self.board.draw_lose(surface)

    def start(self, start):
        self.board.players["HU"] = start
        self.board.players["COMP"] = -start
        self.run = True

    def restart(self):
        self.board.restart()
        self.run = False

    def ai_turn(self):
        if self.board.turn == self.board.players["COMP"] and self.start:
            depth = len(self.board.get_empty())
            if depth == 0 or self.board.is_ended():
                return
            if depth == 9:
                self.board.move_to(1, 1, self.board.players["COMP"])
            else:
                result = self.ai.minimax(self.board, depth, self.board.players["COMP"])
                self.board.move_to(result[0], result[1], self.board.players["COMP"])
