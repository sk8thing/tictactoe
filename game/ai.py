from math import inf


def evaluate(board):
    if board.check_win(board.players["COMP"]):
        score = board.players["COMP"]
    elif board.check_win(board.players["HU"]):
        score = board.players["HU"]
    else:
        score = 0
    return score


class COMP:
    def minimax(self, board, depth, player):
        if player == board.players["COMP"]:
            best = [-1, -1, -inf] if board.players["COMP"] == 1 else [-1, -1, +inf]
        else:
            best = [-1, -1, +inf] if board.players["HU"] == -1 else [-1, -1, -inf]

        if depth == 0 or board.is_ended():
            score = evaluate(board)
            return [-1, -1, score]

        for cell in board.get_empty():
            x, y = cell[0], cell[1]
            board.board[x][y] = player
            score = self.minimax(board, depth - 1, -player)
            board.board[x][y] = 0
            score[0], score[1] = x, y

            if player == board.players["COMP"]:
                if board.players["COMP"] == 1:
                    if score[2] > best[2]:
                        best = score
                else:
                    if score[2] < best[2]:
                        best = score
            else:
                if board.players["HU"] == -1:
                    if score[2] < best[2]:
                        best = score
                else:
                    if score[2] > best[2]:
                        best = score
        return best
