with open("marks.txt", "r") as infile:
    lines = infile.readlines()
with open("results.txt", "w") as outfile:
    for line in lines:
        parts = line.split()
        name = parts[0]
        score1 = int(parts[1])
        score2 = int(parts[2])
        score3 = int(parts[3])
        avg = (score1 + score2 + score3) / 3
        outfile.write(f"{name}: {round(avg, 1)}\n")
print("Averages calculated and saved to 'results.txt'!")
