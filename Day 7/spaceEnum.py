path = []
dirs = {}
filePaths = {}
with open("input.txt", encoding = "utf-8") as f:
	for line in f:
		line = line.strip().split()

		if(line[0] == '$'): # Command
			if(line[1] == "cd"): # Change directory
				if(line[2] == ".."):
					path.pop() # Move a level out (remove from path)
				else: # Move a level in
					path.append(line[2]) # Add directory to path; this way we always have an up-to-date hierarchical path
				#print("Path:", path)
		else:
			if(line[0].isnumeric()): # If the first part of the line is numeric, it's a file size, which is what we need to track
				if(line[1] in filePaths):
					for p in filePaths[line[1]]:
						if(p == path):
							print("Same path as before, ignore file")
							continue
					
				for dir in path: # A file adds to the total size of every folder in the path, starting from root
					if(dir in dirs.keys()): # If we already track that directory, just add the file size
						dirs[dir] += int(line[0])
					else: # Otherwise, add the new directory to our dictionary
						dirs[dir] = int(line[0])
					#print("Added", int(line[0]), "to", dir)

				if(line[1] in filePaths):
					filePaths[line[1]].append(path.copy())
				else:
					filePaths[line[1]] = [path.copy()]

print(filePaths)
dirSum = 0
for dir in dirs:
	if(dirs[dir] <= 100000):
		#print(dir, dirs[dir])
		dirSum += dirs[dir] # Sum up folders with less than 100k size

print(dirSum)