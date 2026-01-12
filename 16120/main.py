c = []
for i in input():
    c.append(i)
    if "".join(c[-4:]) == "PPAP":
        for _ in range(3):
            c.pop()

print("PPAP" if "".join(c) == "P" else "NP")