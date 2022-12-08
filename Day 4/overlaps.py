fullOverlaps = 0
totalOverlaps = 0
with open("input.txt", encoding = "utf-8") as f:
	for line in f:
		sections = line.strip().split(",")
		sections[0] = sections[0].split("-") # Get both intervals in separate lists
		sections[1] = sections[1].split("-")

		# Check for full overlaps - when one interval completely includes the other
		if int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1]): # Either interval could overlap the other
			fullOverlaps += 1
		elif int(sections[0][0]) >= int(sections[1][0]) and int(sections[0][1]) <= int(sections[1][1]):
			fullOverlaps += 1
		else:
			pass

		# Check for any overlaps at all
		if not (int(sections[0][1]) < int(sections[1][0]) or int(sections[0][0]) > int(sections[1][1])): # If they don't overlap, the first interval is either fully below or fully above the second
			totalOverlaps += 1 # If these two conditions aren't true, they overlap

print(fullOverlaps, totalOverlaps)