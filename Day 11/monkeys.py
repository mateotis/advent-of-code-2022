monkeys = {}
monkey = -1
operations = []
tests = []

with open("input.txt", encoding = "utf-8") as f: # First part of the puzzle
	for line in f:
		line = line.strip()
		if("Monkey " in line):
			monkey += 1
			monkeys[monkey] = []
			#print(monkeys)
		elif("Starting items: " in line):
			items = line[len("Starting items: "):].split(", ") # Get list of items
			for i in range(0, len(items)):
				monkeys[monkey].append(int(items[i]))
		elif("Operation: " in line):
			operations.append(line[len("Operation: "):]) # Save operation, which will be exec()'d
		elif("Test: " in line):
			tests.append([int(line.split()[-1])]) # The last number in the line is the test division number
		elif("If true: " in line):
			tests[monkey].append(int(line[-1])) # The last number is the monkey the item will be thrown to, which we add to the inner list created in the previous iteration
		elif("If false: " in line):
			tests[monkey].append(int(line[-1])) # Ditto
print(monkeys)
print(operations)
print(tests)

inspections = []
for i in range(monkey + 1):
	inspections.append(0)
print(inspections)

for round in range(20): # Playing 20 rounds of monkey-in-the-middle!
	for monkey in monkeys:
		for item in monkeys[monkey]:
			old = item
			exec(operations[monkey]) # Do the operation assigned to that monkey
			item = new // 3 # Divide worry level by 3

			inspections[monkey] += 1 # Track how many times each monkey inspected items

			trueMonkey = tests[monkey][1] # The monkey throws the item
			falseMonkey = tests[monkey][2]
			if(item % tests[monkey][0] == 0): # To one of two options, decided by the test
				monkeys[trueMonkey].append(item)
			else:
				monkeys[falseMonkey].append(item)

		monkeys[monkey] = [] # Empty out the current monkey list, as it has thrown away everything

	print(round + 1, monkeys)

for i in range(len(inspections)):
	print("Monkey", i, "inspections:", inspections[i])

sortedInspections = sorted(inspections)
monkeyBusiness = sortedInspections[-1] * sortedInspections[-2] # Find the two largest inspection counts and multiply them together
print(monkeyBusiness)

monkeys = {}
monkey = -1
operations = []
tests = []

with open("input.txt", encoding = "utf-8") as f: # Second part of the puzzle
	for line in f:
		line = line.strip()
		if("Monkey " in line):
			monkey += 1
			monkeys[monkey] = []
		elif("Starting items: " in line):
			items = line[len("Starting items: "):].split(", ") # Get list of items
			for i in range(0, len(items)):
				monkeys[monkey].append(int(items[i]))
		elif("Operation: " in line):
			operations.append(line[len("Operation: "):]) # Save operation, which will be exec()'d
		elif("Test: " in line):
			tests.append([int(line.split()[-1])]) # The last number in the line is the test modulo
		elif("If true: " in line):
			tests[monkey].append(int(line[-1])) # The last number is the monkey the item will be thrown to, which we add to the inner list created in the previous iteration
		elif("If false: " in line):
			tests[monkey].append(int(line[-1])) # Ditto
print(monkeys)
print(operations)
print(tests)

inspections = []
for i in range(monkey + 1):
	inspections.append(0)
print(inspections)
# Same code up to this point

# To avoid our worry values becoming completely unmanageable, we figure out the common modulo of all our monkeys
# We can get the remainder of each worry value by that number, and it won't change any calculation results WHILE keeping calculation times manageable
modulo = 1
for test in tests: # 
	modulo *= test[0]
print("Common modulo:", modulo)

for round in range(10000): # Except we play 10000 rounds!
	for monkey in monkeys:
		for item in monkeys[monkey]:
			old = item
			exec(operations[monkey]) # Do the operation assigned to that monkey
			item = new % modulo # And we no longer divide worry levels by 3, instead we use the cool modulo
			
			inspections[monkey] += 1 # Track how many times each monkey inspected items

			trueMonkey = tests[monkey][1] # The monkey throws the item
			falseMonkey = tests[monkey][2]
			if(item % tests[monkey][0] == 0): # To one of two options, decided by the test
				monkeys[trueMonkey].append(item)
			else:
				monkeys[falseMonkey].append(item)

		monkeys[monkey] = [] # Empty out the current monkey list, as it has thrown away everything

	if(round + 1 == 1 or round + 1 == 20 or (round + 1) % 1000 == 0):
		print("== After round", round + 1, "==")
		print(monkeys)
		for i in range(len(inspections)):
			print("Monkey", i, "inspections:", inspections[i])

for i in range(len(inspections)):
	print("Monkey", i, "inspections:", inspections[i])

sortedInspections = sorted(inspections)
monkeyBusiness = sortedInspections[-1] * sortedInspections[-2] # Find the two largest inspection counts and multiply them together
print(monkeyBusiness)