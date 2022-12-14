cycle = 0
X = 1
cycleInterval = []

with open("input.txt", encoding = "utf-8") as f: # First part of the puzzle
	for line in f:
		line = line.strip()

		if(line == "noop"):
			if(cycle == 19 or (cycle - 19) % 40 == 0): # We're looking for the value DURING the 20th/60th/etc cycle, so we must check the value AFTER the previous cycle
				cycleInterval.append(X)
			cycle += 1
		else:
			add = int(line.split()[1])
			for i in range(2): # Simulate how addx takes two cycles and track the X value during each cycle
				if(i == 0): # First cycle it does nothing
					if(cycle == 19 or (cycle - 19) % 40 == 0):
						cycleInterval.append(X)
					cycle += 1
				else: # After second cycle, we add the value to X
					if(cycle == 19 or (cycle - 19) % 40 == 0):
						cycleInterval.append(X)
					cycle += 1
					X += add

print(cycleInterval)
sum = 0
for i in range(len(cycleInterval)):
	if(i == 0):
		signalStrength = cycleInterval[i] * 20
		print("Signal strength at", 20, signalStrength)
	else:
		signalStrength = cycleInterval[i] * (i * 40 + 20)
		print("Signal strength at", i * 40 + 20, signalStrength)

	
	sum += signalStrength
print(sum)

cycle = 1
X = 1
sprite = [X - 1, X, X + 1] # The sprite is the three pixels wide, X always specifies the middle

with open("input.txt", encoding = "utf-8") as f: # Second part of the puzzle
	for line in f:
		line = line.strip()

		if(line == "noop"):
			if(cycle - 1 in sprite): # The cycle is 1-indexed, but positions are 0-indexed, hence the -1 adjustment
				print("#", end="") # If the pixel is "lit", draw an #
			else:
				print(" ", end="") # Otherwise, don't draw anything

			if(cycle % 40 == 0): # The CRT screen is 40 pixels wide, switch to a new line afterwards
				print("\n")
				cycle = 1
			else:
				cycle += 1
			
		else:
			add = int(line.split()[1])
			for i in range(2): # Simulate how addx takes two cycles and track the X value during each cycle
				if(i == 0): # First cycle it does nothing
					if(cycle - 1 in sprite):
						print("#", end="")
					else:
						print(" ", end="")
					if(cycle % 40 == 0):
						print("\n")
						cycle = 1
					else:
						cycle += 1
					
				else: # After second cycle, we add the value to X
					if(cycle - 1 in sprite):
						print("#", end="")
					else:
						print(" ", end="")

					X += add # Move the sprite and update it
					sprite = [X - 1, X, X + 1]

					if(cycle % 40 == 0): # The order of the drawing and cycle updates are important!
						print("\n")
						cycle = 1
					else:
						cycle += 1