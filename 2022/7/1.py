# Import the defaultdict class from the collections module
from collections import defaultdict

# Read the lines from the input file
with open("input.txt") as f:
    lines = f.readlines()

# Create an empty list for the path and a defaultdict for the directories
path = []
dirs = defaultdict(int)

# Iterate through the lines of the file
for line in lines:
    # Split the line into words
    words = line.split()

    # If the line starts with "$ cd", update the current directory
    if words[0] == "$" and words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])

    # If the line starts with a file size, update the directories
    elif words[0] != "dir" and words[0] != "$":
        for i in range(len(path)):
            dirs[tuple(path[: i + 1])] += int(words[0])

# Compute the total size of the files below or equal to 100,000
total_size = sum((size for size in dirs.values() if size <= 100000))

# Print the total size
print(total_size)

# Compute the required size
required = 30000000 - (70000000 - dirs[("/",)])

# Compute the minimum size that is equal to or greater than the required size
min_size = min(size for size in dirs.values() if size >= required)

# Print the minimum size
print(min_size)
