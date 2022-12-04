with open("input.txt") as file:
    elfpairs = file.read().splitlines()


def is_inside(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


def has_overlap(a, b):
    return a[1] >= b[0] and a[0] <= b[1]


def one():
    count = 0
    for elf in elfpairs:
        elfranges = elf.split(',')
        a1, a2, b1, b2 = elf.replace('-', ',').split(',')
        a, b = ((int(a1), int(a2)), (int(b1), int(b2)))
        count += 1 if is_inside(a, b) or is_inside(b, a) else 0
    print(count)


def two():
    count = 0
    for elf in elfpairs:
        elfranges = elf.split(',')
        a1, a2, b1, b2 = elf.replace('-', ',').split(',')
        a, b = ((int(a1), int(a2)), (int(b1), int(b2)))
        count += 1 if has_overlap(a,b) or has_overlap(b, a) else 0
    print(count)
