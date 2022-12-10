directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}

def move(X, d):
  return (X[0]+d[0], X[1]+d[1])

def solution(lines, knots=10):
    knotlist = [(0, 0)] * knots
    visited = set(knotlist)

    for l in lines.split("\n"):
        direction, steps = l.split()
        for _ in range(int(steps)):
            knotlist[0] = move(knotlist[0], directions[direction])

            # To solve problem 2, we loop over each knot
            # Input to function is adapted to suit both problems
            for k in range(1, len(knotlist)):
                diff = [knotlist[k - 1][i] - knotlist[k][i] for i in (0, 1)]
                if abs(max(diff, key=abs)) > 1:
                    knotlist[k] = move(knotlist[k], [x // (abs(x) or 1) for x in diff])
            visited.add(knotlist[-1])

    return len(visited)


with open("input.txt") as f:
    lines = f.read()
    print(solution(lines, knots=2))
    print(solution(lines, knots=10))
