def findpos(buffer: str, caplen: int) -> int:
    for i in range(len(buffer)):
        capture = z[i:i + caplen]
        if (len(set(capture))) == caplen:
            return i + caplen


with open("input.py") as f:
    z = f.read()
    print("Solution one: %s" % findpos(z, 4))
    print("Solution two: %s" % findpos(z, 14))
