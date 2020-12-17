
fhand = input('')
counts = dict()

line = fhand.lower()
words = line.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)
