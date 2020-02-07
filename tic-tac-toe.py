import numpy as np
import random

def create_board():
	return np.zeros((3,3), dtype=int)

def place(board, player, position):
	if board[position] == 0:
		board[position] = player

def possibilities(board):
	out = list()
	x,y = np.where(board==0)
	for i in range(len(x)):
		out.append((x[i],y[i]))
	return(out)

def random_place(board, player):
	if len(possibilities(board)) != 0:
		pos = random.choice(possibilities(board))
		place(board, player, pos)

def row_win(board, player):
	if np.any(np.all(board == player,1)==True):
		return True
	return False

def coll_win(board, player):
	if np.any(np.all(board == player, 0) == True):
		return True
	return False

def diag_win(board, player):
	if np.all(board.diagonal() == player):
		return True
	return False

def evaluate(board):
	winner = 0
	for player in [1, 2]:
		checks = [row_win(board,player),coll_win(board,player), diag_win(board,player)]
		if True in checks:
			winner = player
	if np.all(board != 0) and winner == 0:
		winner = -1
	return winner

def play_game():
	bo = create_board()
	while True:
		random_place(bo, 1)
		if evaluate(bo) != 0:
			return evaluate(bo)
		random_place(bo, 2)
		if evaluate(bo) != 0:
			return evaluate(bo)

def play_strategic_game():
	bo = create_board()
	place(bo, 1, (1,1))
	while True:
		random_place(bo, 2)
		if evaluate(bo) != 0:
			return evaluate(bo)
		random_place(bo, 1)
		if evaluate(bo) != 0:
			return evaluate(bo)


if __name__ == '__main__':
	random.seed(1)

	results_normal = list()
	for _ in range(1000):
		results_normal.append(play_game())
	print(f"Normal:\nPlayer 1: {results_normal.count(1)}\nPlayer 2: {results_normal.count(2)}\nDraw: {results_normal.count(-1)}\n")

	random.seed(1)

	results_strategic = list()
	for _ in range(1000):
		results_strategic.append(play_strategic_game())
	print(f"Strategic:\nPlayer 1: {results_strategic.count(1)}\nPlayer 2: {results_strategic.count(2)}\nDraw: {results_strategic.count(-1)}")