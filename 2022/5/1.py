from copy import deepcopy


def results(astack):
    result = ""
    for stack in astack:
        print(stack)
        if stack:
            result += stack.pop()
    return(result)


with open("input.txt") as f:
    stacks = []
    stacks.append([])
    stacks.append(["N", "B", "D", "T", "V", "G", "Z", "J"])
    stacks.append(["S", "R", "M", "D", "W", "P", "F"])
    stacks.append(["V", "C", "R", "S", "Z"])
    stacks.append(["R", "T", "J", "Z", "P", "H", "G"])
    stacks.append(["T", "C", "J", "N", "D", "Z", "Q", "F"])
    stacks.append(["N", "V", "P", "W", "G", "S", "F", "M"])
    stacks.append(["G", "C", "V", "B", "P", "Q"])
    stacks.append(["Z", "B", "P", "N"])
    stacks.append(["W", "P", "J"])
    commands = []
    s1 = deepcopy(stacks)
    s2 = deepcopy(stacks)

    while (True):
        line = f.readline()
        if not line:
            break
        command = int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5].strip())
        commands.append(command)

    for command in commands:
        amount = int(command[0])
        fromstack = int(command[1])
        tostack = int(command[2])
        for i in range(amount):
            crate = s1[fromstack].pop()
            s1[tostack].append(crate)

    for command in commands:
        tempstack = []
        amount = int(command[0])
        fromstack = int(command[1])
        tostack = int(command[2])
        for i in range(amount):
            crate = s2[fromstack].pop()
            tempstack.append(crate)
        tempstack.reverse()
        s2[tostack] += tempstack

    print(results(s1))
    print(results(s2))