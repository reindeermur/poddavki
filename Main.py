#!/usr/bin/env python

# Импортируем библиотеку

from Board import Board
from ScoreBoard import ScoreBoard

WIN_WIDTH = 792  # Ширина создаваемого окна
WIN_HEIGHT = 576 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную


def main():

    board = Board()
    score_board = ScoreBoard()

    # while 1:  # Основной цикл программы
    #     for e in pygame.event.get():
    #         handle_event(e, board)  # Обрабатываем события
    #         if e.type == pygame.QUIT:
    #             exit()
    #
    #     board.draw()
    #     score_board.draw()
    #     pygame.display.update()  # обновление и вывод всех изменений на экран


def handle_event(event, board):
    """Обработчик событий"""
    # if event.type == pygame.MOUSEBUTTONUP:
    #     pos = pygame.mouse.get_pos()
    #     if (0 < pos[0] // 72 < 8) and (0 < pos[1] // 72 < 8):#ЕБАНЫЙ ГОВНОКОД
    #          print(pos[0] // 72, pos[1] // 72, ":")
    #          print(pos[0] // 72 + 1, pos[1] // 72 - 1)
    #          print(pos[0] // 72 - 1, pos[1] // 72 - 1)
    #          print(pos[0] // 72 + 1, pos[1] // 72 + 1)
    #          print(pos[0] // 72 - 1, pos[1] // 72 + 1)


if __name__ == "__main__":
    main()
