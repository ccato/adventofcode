counts = list()
with open("input.txt") as elfcals:
    for elfline in elfcals.read().split('\n\n'):
        counts.append(sum(int(x) for x in elfline.split('\n')))
    counts.sort(reverse=True)
    print(counts[0:3])
