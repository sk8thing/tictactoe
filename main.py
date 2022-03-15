import pygame
import sys
from game import GAME


def main_game():
    screen = pygame.display.set_mode((600, 600))
    game = GAME()
    pygame.display.set_caption("X && O")
    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False) and not game.run:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if 50 < x < 250 and 150 < y < 350:
                    game.start(1)
                elif 350 < x < 550 and 150 < y < 350:
                    game.start(-1)
            elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (True, False, False) and game.board.turn == game.board.players["HU"]:
                x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                row, col = x // 200, y // 200
                game.board.move_to(row, col, game.board.players["HU"])
            if e.type == pygame.KEYDOWN and e.key == pygame.K_r and game.board.is_ended():
                game.restart()

        screen.fill("White")
        game.update(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main_game()
