import numpy
import pygame


class BOARD:
    def __init__(self):
        self.__ROWS, self.__COLUMNS = 3, 3
        self.board = numpy.zeros((self.__ROWS, self.__COLUMNS))
        self.turn = 1
        self.players = {
            "HU": 0,
            "COMP": 0
        }
        self.x_surface = pygame.image.load('game/assets/X.png').convert_alpha()
        self.o_surface = pygame.image.load('game/assets/O.png').convert_alpha()
        self.board_surface = pygame.image.load('game/assets/Board.png').convert_alpha()

    def move_to(self, row, col, player):
        if self.can_move_to(row, col) and not self.is_ended():
            self.board[row][col] = player
            self.turn = -self.turn
            return True
        return False

    def get_empty(self):
        blocks = []
        for row in range(self.__ROWS):
            for col in range(self.__COLUMNS):
                if self.can_move_to(row, col):
                    blocks.append([row, col])
        return blocks

    def can_move_to(self, row, col):
        return self.board[row][col] == 0

    def is_full(self):
        for row in range(self.__ROWS):
            for col in range(self.__COLUMNS):
                if self.board[row][col] == 0:
                    return False
        return True

    def is_ended(self):
        return self.check_win(self.players["COMP"]) or self.check_win(self.players["HU"]) or self.is_full()

    def check_win(self, player):
        win_cases = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return True if [player, player, player] in win_cases else False

    def restart(self):
        self.turn = 1
        for row in range(self.__ROWS):
            for col in range(self.__COLUMNS):
                self.board[row][col] = 0

    def draw_board(self, surface):
        surface.blit(self.board_surface, (0, 0))
        for row in range(self.__ROWS):
            for col in range(self.__COLUMNS):
                if self.board[row][col] == 1:
                    surface.blit(self.x_surface, (row * 200, col * 200))
                elif self.board[row][col] == -1:
                    surface.blit(self.o_surface, (row * 200, col * 200))

    def draw_menu(self, surface):
        font = pygame.font.Font(None, 30).render("X starts first, O starts second.", False, "Black")
        surface.blit(font, (160, 450))
        surface.blit(self.x_surface, (50, 150))
        surface.blit(self.o_surface, (350, 150))

    def draw_lose(self, surface):
        if self.is_ended() and not self.is_full():
            if self.turn == -1:
                font = pygame.font.Font(None, 30).render(f'X is the winner.', False, "Black")
            elif self.turn == 1:
                font = pygame.font.Font(None, 30).render(f'O is the winner.', False, "Black")
            surface.blit(font, (220, 300))
        else:
            font = pygame.font.Font(None, 30).render(f'Tie.', False, "Black")
            surface.blit(font, (280, 300))
