import pygame
import chess
import math

X = 800
Y = 800
screen = pygame.display.set_mode((X, Y))
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

b = chess.Board()

pieces = {
    'p': pygame.image.load('b_pawn.png'),
    'n': pygame.image.load('b_knight.png'),
    'b': pygame.image.load('b_bishop.png'),
    'r': pygame.image.load('b_rook.png'),
    'q': pygame.image.load('b_queen.png'),
    'k': pygame.image.load('b_king.png'),
    'P': pygame.image.load('w_pawn.png'),
    'N': pygame.image.load('w_knight.png'),
    'B': pygame.image.load('w_bishop.png'),
    'R': pygame.image.load('w_rook.png'),
    'Q': pygame.image.load('w_queen.png'),
    'K': pygame.image.load('w_king.png'),
}


def update(screen_, board):
    for i in range(64):
        piece = board.piece_at(i)
        if piece is not None:
            screen_.blit(pieces[str(piece)], ((i % 8) * 100, 700 - (i // 8) * 100))

    for i in range(1, 8):
        pygame.draw.line(screen_, WHITE, (0, i * 100), (800, i * 100))
        pygame.draw.line(screen_, WHITE, (i * 100, 0), (i * 100, 800))

    pygame.display.flip()


def main(board_):
    screen.fill(GREY)
    pygame.display.set_caption('Chess')

    index_moves = []

    status = True
    while status:
        # update screen
        update(screen, board_)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                status = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(GREY)
                pos = pygame.mouse.get_pos()

                square = (math.floor(pos[0] / 100), math.floor(pos[1] / 100))
                index = (7 - square[1]) * 8 + (square[0])

                if index in index_moves:

                    # noinspection PyUnboundLocalVariable
                    move = moves[index_moves.index(index)]

                    board_.push(move)

                    # noinspection PyUnusedLocal
                    index = None
                    index_moves = []

                else:
                    piece = board_.piece_at(index)
                    if piece is None:
                        pass
                    else:
                        all_moves = list(board_.legal_moves)
                        moves = []
                        for move in all_moves:
                            if move.from_square == index:
                                moves.append(move)

                                to = move.to_square

                                TX = 100 * (to % 8)
                                TY = 100 * (7 - to // 8)

                                pygame.draw.rect(screen, BLUE, pygame.Rect(TX, TY, 100, 100), 5)

                        index_moves = [a.to_square for a in moves]

        if board_.outcome() is not None:
            print(board_.outcome())
            status = False
            print(board_)
            if "False" in str(board_.outcome()):
                print("\nBLACK SIDE WON!\n")
            else:
                print("\nWHITE SIDE WON!\n")
    pygame.quit()


if __name__ == "__main__":
    main(b)
