with open("input.txt", encoding = "utf-8") as f:
	datastream = f.readline().strip()

# First part of the puzzle
marker = datastream[0:4] # Create initial marker from the first four chars
if(len(set(marker)) == 4): # Test this with the set method - if all chars are unique, the set will have length 4
	print(marker)

for i in range(4, len(datastream)):
	marker = marker[1:] + datastream[i] # Advance char by char: remove the first, add the newest
	if(len(set(marker)) == 4): # Test every marker
		print("Found unique marker", marker, "ending at index", i + 1) # Print the first unique four-char combination
		break

# Second part of the puzzle
marker = datastream[0:14] # The start-of-message marker consists of 14 chars 
if(len(set(marker)) == 14): # Test this with the set method - if all chars are unique, the set will have length 14
	print(marker)

for i in range(14, len(datastream)): # Same iteration code as before
	marker = marker[1:] + datastream[i] # Advance char by char: remove the first, add the newest
	if(len(set(marker)) == 14): # Test every marker
		print("Found unique marker", marker, "ending at index", i + 1) # Print the first unique 14-char combination
		break