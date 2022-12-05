from copy import deepcopy


def results(astack):
    result = ""
    for stack in astack:
        print(stack)
        if stack:
            result += stack.pop()
    return (result)


def movestacks(stackset: list, commandset: list, multiples=False) -> list:
    for command in commandset:
        amount = int(command[0])
        fromstack = int(command[1])
        tostack = int(command[2])
        tempstack = []
        if multiples is True:
            for i in range(amount):
                crate = stackset[fromstack].pop()
                tempstack.append(crate)
            tempstack.reverse()
            stackset[tostack] += tempstack
        else:
            for i in range(amount):
                crate = stackset[fromstack].pop()
                stackset[tostack].append(crate)
    return stackset


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

    s1 = movestacks(s1, commands)
    s2 = movestacks(s2, commands, True)
    print(results(s1))
    print(results(s2))
