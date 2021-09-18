f = open("million.txt", "wt")
for i in range(0, 10_000_000):
    f.write(f"{i}\n")

f.close()