alphabet = ""
for i in range(26): # Put alphabet string together, starting with lowercase letters
	alphabet += chr(97 + i)
for i in range(26): # Then add the uppercase letters
	alphabet += chr(65 + i)

print(alphabet)

prioSum = 0
with open("input.txt", encoding = "utf-8") as f: # First part of the puzzle
	for line in f:
		line = line.strip()
		compartments = [line[:len(line) // 2], line[len(line) // 2:]] # Split rucksack contents into two equal halves

		commonItem = ''.join(set(compartments[0]).intersection(compartments[1])) # Perform a set intersection to find the common item (should only be one) between the two compartments
		prioSum += alphabet.find(commonItem) + 1 # The priority of each letter is their position in the string plus 1

print(prioSum)

prioSum = 0
with open("input.txt", encoding = "utf-8") as f: # Second part of the puzzle
	i = 0
	group = []
	for line in f:
		group.append(line.strip())
		i += 1
		if(i % 3 == 0): # Once we gathered three elves in a group, do the calculations
			commonItem = ''.join(set(group[0]).intersection(group[1], group[2])) # Find the common item type in all three rucksacks
			prioSum += alphabet.find(commonItem) + 1
			group = [] # And finally, empty out this group so we can continue with the next one

print(prioSum)
