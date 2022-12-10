from textwrap import wrap
# Read the instructions from input.txt
with open("input.txt") as f:
  instructions = f.read().splitlines()

# Initialize a dictionary to store the values of the X register at each cycle
X_values = {}

# Initialize the X register and the cycle counter
X = 1
cycle = 0

# Loop through the instructions
for inst in instructions:
  # If the instruction is "noop", increment the cycle counter and store the current value of X
  if inst.startswith("noop"):
    cycle += 1
    X_values[cycle] = X

  # If the instruction is "addx", increment the cycle counter, store the current value of X,
  # increment the cycle counter again, store the current value of X again, and then
  # update the value of X according to the instruction
  else:
    cycle += 1
    X_values[cycle] = X
    cycle += 1
    X_values[cycle] = X
    X += int(inst.split()[1])

# Calculate and print the sum of the signal strengths at the specified cycles
print(sum(X_values[k] * k for k in range(20, 221, 40)))

# Build the string representation of the screen
s = "".join("#" if X_values[cycle] - 1 <= (cycle % 40 - 1) % 40 <= X_values[cycle] + 1 else "." for cycle in range(1, 241))

# Print the screen by wrapping the string at 40 characters and printing each line
print("\n".join(wrap(s, 40)))
