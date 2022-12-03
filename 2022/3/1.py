import string

lcp = {l: i + 1 for i, l in enumerate(string.ascii_lowercase)}
ucp = {l: i + 27 for i, l in enumerate(string.ascii_uppercase)}
priority = {**lcp, **ucp}
with open("input.txt") as file:
    sacks = [sack[:-1] for sack in file.readlines()]

def one(sacks: list[str]) -> int:
    tot = 0
    for line in sacks:
        first = set(line[:int(len(line) // 2)])
        second = set(line[int(len(line) // 2):])
        item = first.intersection(second).pop()
        tot += priority[item]
    return tot


def two(sacks: list[str]) -> int:
    tot = 0
    for i in range(0, len(sacks), 3):
        sack_sets = []
        for j in range(i + 1, i + 3):
            sack_set = set(sacks[j])
            sack_sets.append(set(sacks[j]))
        shared = set(sacks[i]).intersection(sack_sets[0], sack_sets[1]).pop()
        tot += priority[shared]
    return tot

print(one(sacks))
print(two(sacks))
