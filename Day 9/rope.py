headPos = [0,0]
tailPos = [0,0]
headMoves = 0
tailMoves = 0
tailPositions = [[0,0]] # List to keep all the positions the tail visited, already contains the starting position

def neighbours(i, j): # Check if the head is next to (or in the same position as) the tail
	if headPos in [[i,j], [i-1,j], [i,j-1], [i-1,j-1], [i+1,j], [i,j+1], [i+1,j+1], [i+1,j-1], [i-1,j+1]]:
		return True
	else:
		return False

with open("input.txt", encoding = "utf-8") as f:
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

			if(neighbours(tailPos[0], tailPos[1]) == False): # If the tail is no longer next to the head, move the tail
				tailMoves += 1
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

				if(tailPos not in tailPositions):
					tailPositions.append(tailPos.copy())

print(tailPositions)
print(headPos)
print(tailPos)
print(headMoves, tailMoves)
print(len(tailPositions))