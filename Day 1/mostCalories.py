calories = [0]

with open("input.txt", encoding = "utf-8") as f:
	for line in f:
		if line == '\n': # Newlines mark new elves, so add a new counter
			calories.append(0)
		else:
			calories[-1] += int(line) # Otherwise, add the calorie count to the current elf's counter (always the last list entry)

print(max(calories)) # Get the highest value
calories.sort() # Sort list in ascending order
print(sum(calories[-3:])) # Get the three highest counts and add them up
