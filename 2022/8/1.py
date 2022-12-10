# Parse the input grid
grid = []
for line in open("input.txt"):
  grid.append(list(line.strip()))

# Count the number of visible trees
count = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    # Check if the current tree is visible from the left
    visible_from_left = True
    for k in range(j):
      if grid[i][k] >= grid[i][j]:
        visible_from_left = False
        break

    # Check if the current tree is visible from the right
    visible_from_right = True
    for k in range(j + 1, len(grid[i])):
      if grid[i][k] >= grid[i][j]:
        visible_from_right = False
        break

    # Check if the current tree is visible from the top
    visible_from_top = True
    for k in range(i):
      if grid[k][j] >= grid[i][j]:
        visible_from_top = False
        break

    # Check if the current tree is visible from the bottom
    visible_from_bottom = True
    for k in range(i + 1, len(grid)):
      if grid[k][j] >= grid[i][j]:
        visible_from_bottom = False
        break

    # If the tree is visible from any direction, increment the count
    if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
      count += 1

# Print the number of visible trees
print(count)
