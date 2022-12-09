trees = []
with open("input.txt", encoding = "utf-8") as f:
	for line in f:
		row = list(line.strip()) # Collect trees into a matrix
		row = [int(i) for i in row]
		trees.append(row)

visible = 0
for i in range(len(trees)): # First part of the puzzle - calculate visibility of each tree from outside
	for j in range(len(trees[i])):
		if(i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[i]) - 1): # The trees on the edges are always visible
			visible += 1
		else:
			hiddenLeft = False
			hiddenRight = False
			hiddenUp = False
			hiddenDown = False
			for k in range(j): # Check from left
				if trees[i][k] >= trees[i][j]:
					hiddenLeft = True
			for k in range(j + 1, len(trees[i])): # Check from right
				if trees[i][k] >= trees[i][j]:
					hiddenRight = True	
			for k in range(i): # Check above
				if trees[k][j] >= trees[i][j]:
					hiddenUp = True
			for k in range(i + 1, len(trees)): # Check below
				if trees[k][j] >= trees[i][j]:
					hiddenDown = True

			if(not hiddenLeft or not hiddenRight or not hiddenUp or not hiddenDown): # If it's not hidden from all four directions, the tree is visible
				visible += 1			

maxScore = 0
for i in range(len(trees)): # Second part of the puzzle - calculating how many trees are visible from each tree
	for j in range(len(trees[i])):
		viewLeft = 0
		viewRight = 0
		viewUp = 0
		viewDown = 0
		for k in range(j - 1, -1, -1): # Check from left - when iterating in a descending order, we have to be extra mindful of the indices
			viewLeft += 1
			if trees[i][k] >= trees[i][j]: # Stop once we hit a tree we can't see past
				break
		for k in range(j + 1, len(trees[i])): # Check from right
			viewRight += 1
			if trees[i][k] >= trees[i][j]:
				break	
		for k in range(i - 1, -1, -1): # Check above
			viewUp += 1
			if trees[k][j] >= trees[i][j]:
				break
		for k in range(i + 1, len(trees)): # Check below
			viewDown += 1
			if trees[k][j] >= trees[i][j]:
				break

		score = viewLeft * viewRight * viewUp * viewDown # Multiply view distances together
		if(score > maxScore):
			maxScore = score

print(visible)
print(maxScore)