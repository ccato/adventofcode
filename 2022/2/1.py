with open("input.txt") as file:
    score = 0
    scoring = {
        'A X': 4, # rock rock = draw + 1 = 4
        'A Y': 8, # rock paper = win + 2 = 8
        'A Z': 3, # rock scissors = loss + 3 = 3
        'B X': 1, # paper rock = loss + 1 = 1
        'B Y': 5, # paper paper = draw + 2 = 4
        'B Z': 9, # paper scissors = win + 3 = 9
        'C X': 7, # scissors rock = win + 1 = 7
        'C Y': 2, # scissors paper = loss + 2 = 2
        'C Z': 6 # scissors scissors = draw + 3 = 6
    }
    lines = file.read()
    print(sum(list(map(lambda x: scoring.get(x), lines.split('\n')))))
