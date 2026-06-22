line_count = 0
word_count = 0
char_count = 0
with open("sample.txt", "r") as file:
    for line in file:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")

