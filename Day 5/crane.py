from copy import deepcopy

stacks = [[], [], [], [], [], [], [], [], []] # We have 9 stacks, so initialise 9 empty lists
moves = []
stacksDone = False
with open("input.txt", encoding = "utf-8") as f:
	for line in f:
		if(line == "\n"): # An empty line separates the stack starting state from the moves
			stacksDone = True
			continue
		if(stacksDone == False):
			for i in range(9): # There can be at most 9 elements in a row
				if(line[i*4] == '['): # The elements start on every 4th character - if the [ is not there, that stack has nothing in this row
					stacks[i].append(line[i*4+1]) # Otherwise, add the element to its stack
		else: # Once the stacks are done, parse the moves
			lineList = line.strip().split()
			moves.append([int(lineList[1]), int(lineList[3]), int(lineList[5])]) # Store the amount of crates moved, the origin, and the destination stacks

print("Starting stacks:", stacks)
stacks2 = deepcopy(stacks) # Make a deep copy of the original stack layout for part two

for move in moves: # First part of the puzzle - crates are moved one-by-one
	amount = move[0]
	origin = move[1] - 1 # -1 to account for the zero-index
	dest = move[2] - 1

	for i in range(amount): # Move as many crates as specified
		crate = stacks[origin].pop(0) # Remove crate from top of the origin stack
		stacks[dest].insert(0, crate) # Add it on top of the dest stack

print("\nFirst part stacks:", stacks)
for stack in stacks:
	print(stack[0], end='') # Get the top crate of each stack

for move in moves: # Second part of the puzzle - multiple crates can be moved at once
	amount = move[0]
	origin = move[1] - 1 # -1 to account for the zero-index
	dest = move[2] - 1

	stacks2[dest][0:0] = stacks2[origin][:amount] # Add all the moved crates to the top of the dest stack at once
	stacks2[origin] = stacks2[origin][amount:] # Remove them from the origin stack

print("\nSecond part stacks:", stacks2)
for stack in stacks2:
	print(stack[0], end='') # Get the top crate of each stack