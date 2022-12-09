headPos = [0,0]
tailPos = [0,0]
headMoves = 0
tailMoves = 0
tailPositions = [[0,0]] # List to keep all the positions the tail visited, already contains the starting position

def neighbours(headPos, tailPos): # Check if the head is next to (or in the same position as) the tail
	i = tailPos[0]
	j = tailPos[1]
	if headPos in [[i,j], [i-1,j], [i,j-1], [i-1,j-1], [i+1,j], [i,j+1], [i+1,j+1], [i+1,j-1], [i-1,j+1]]:
		return True
	else:
		return False

def move(headPos, tailPos):
	if(headPos[0] > tailPos[0] and headPos[1] == tailPos[1]): # Move right
		tailPos[0] += 1
	elif(headPos[0] > tailPos[0] and headPos[1] > tailPos[1]): # Move diagonally up-right
		tailPos[0] += 1
		tailPos[1] += 1
	elif(headPos[0] < tailPos[0] and headPos[1] == tailPos[1]): # Move left
		tailPos[0] -= 1
	elif(headPos[0] < tailPos[0] and headPos[1] > tailPos[1]): # Move diagonally up-left
		tailPos[0] -= 1
		tailPos[1] += 1
	elif(headPos[0] == tailPos[0] and headPos[1] > tailPos[1]): # Move up
		tailPos[1] += 1
	elif(headPos[0] == tailPos[0] and headPos[1] < tailPos[1]): # Move down
		tailPos[1] -= 1
	elif(headPos[0] > tailPos[0] and headPos[1] < tailPos[1]): # Move diagonally down-right
		tailPos[0] += 1
		tailPos[1] -= 1
	elif(headPos[0] < tailPos[0] and headPos[1] < tailPos[1]): # Move diagonally down-left
		tailPos[0] -= 1
		tailPos[1] -= 1
	else:
		pass # This should never happen

with open("input.txt", encoding = "utf-8") as f: # First part of the puzzle - one head, one tail
	for line in f:
		lineList = line.strip().split()
		direction = lineList[0]
		steps = int(lineList[1])

		for i in range(steps):
			headMoves += 1
			if(direction == "R"): # Move the head
				headPos[0] += 1
			elif(direction == "L"):
				headPos[0] -= 1
			elif(direction == "U"):
				headPos[1] += 1
			elif(direction == "D"):
				headPos[1] -= 1

			if(neighbours(headPos, tailPos) == False): # If the tail is no longer next to the head, move the tail
				tailMoves += 1
				move(headPos, tailPos)

				if(tailPos not in tailPositions):
					tailPositions.append(tailPos.copy())

print(headPos)
print(tailPos)
print(headMoves, tailMoves)
print(len(tailPositions))

knots = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
headMoves = 0
tailMoves = 0
tailPositions = [[0,0]]

with open("input.txt", encoding = "utf-8") as f: # Second part of the puzzle - ten(!) knots total
	for line in f:
		lineList = line.strip().split()
		direction = lineList[0]
		steps = int(lineList[1])

		for i in range(steps):
			headMoves += 1
			if(direction == "R"): # Move the head
				knots[0][0] += 1
			elif(direction == "L"):
				knots[0][0] -= 1
			elif(direction == "U"):
				knots[0][1] += 1
			elif(direction == "D"):
				knots[0][1] -= 1

			for i in range(len(knots) - 1):
				if(neighbours(knots[i], knots[i+1]) == False):
					move(knots[i], knots[i+1])

					if(i + 1 == 9): # The last knot is the tail
						tailMoves += 1

			if(knots[9] not in tailPositions):
				tailPositions.append(knots[9].copy())

for knot in knots:
	print(knot)
print(headMoves, tailMoves)
print(len(tailPositions))