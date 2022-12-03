def fixLine(line):
    wins = {'A':'Y','B':'Z','C':'X'}
    draws = {'A':'X','B':'Y','C':'Z'}
    losses = {'A':'Z','B':'X','C':'Y'}
    moves = line.split(' ')
    if moves[1] == 'X':
        return "%s %s" % (moves[0],losses.get(moves[0]))
    if moves[1] == 'Y':
        return "%s %s" % (moves[0],draws.get(moves[0]))
    else:
        return "%s %s" % (moves[0],wins.get(moves[0]))

with open("input.txt") as file:
    scoring = {'A X': 4,'A Y': 8,'A Z': 3,'B X': 1,'B Y': 5,'B Z': 9,'C X': 7,'C Y': 2,'C Z': 6 }
    lines = file.read()
    print(sum(list(map(lambda x: scoring.get(x), list(map(lambda x: fixLine(x), lines.split('\n')))))))
