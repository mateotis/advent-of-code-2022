# Dictionaries to store move mapping and move scores
oppMoves = {"A": "rock", "B": "paper", "C": "scissors"}
playerMoves = {"X": "rock", "Y": "paper", "Z": "scissors"}
moveScores = {"rock": 1, "paper": 2, "scissors": 3}
results = {"X": 0, "Y": 3, "Z": 6}

def scoring(opp, player): # To simplify the code, we send the textual mapping ("rock", "paper", "scissors") of the move letters to this function
	if(opp == player):
		return 3 # Tie
	elif (opp == "rock" and player == "scissors") or (opp == "paper" and player == "rock") or (opp == "scissors" and player == "paper"): # All the losing combos
		return 0 # Loss
	else: # No need to write out all the winning combos, it's just the rest of this
		return 6 # Win

def pickMove(opp, result): # Pick the player's move based on what the opponent picked and what result we want
	moves = ["rock", "paper", "scissors"]
	for move in moves: # We only have three moves, go over each and check if they give us the desired result
		if(scoring(oppMoves[opp], move) == results[result]): # If a move does, return it
			return move

score = 0
with open("input.txt", encoding = "utf-8") as f: # First part of the puzzle
	for line in f:
		opponent, player = line.strip().split(" ") # Put both moves into variables
		score += scoring(oppMoves[opponent], playerMoves[player]) + moveScores[playerMoves[player]] # Add round and move scores together each round

print(score)

score = 0
with open("input.txt", encoding = "utf-8") as f: # Second part of the puzzle
	for line in f:
		opponent, result = line.strip().split(" ") # Now the second value stands for the result we need to get
		player = pickMove(opponent, result)
		score += results[result] + moveScores[player] # Tallying up happens the same way: round result + move score

print(score)
