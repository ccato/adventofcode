with open("input.txt") as file:
    scoring = {'A X': 4,'A Y': 8,'A Z': 3,'B X': 1,'B Y': 5,'B Z': 9,'C X': 7,'C Y': 2,'C Z': 6}
    lines = file.read()
    print(sum(list(map(lambda x: scoring.get(x), lines.split('\n')))))
