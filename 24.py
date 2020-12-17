
phrase =' thts the password 123!,cried the special Agent.\nSo i fled .'
counts = dict()

line = phrase.lower()
words = line.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
for count in counts:
    print(count,counts[count])
