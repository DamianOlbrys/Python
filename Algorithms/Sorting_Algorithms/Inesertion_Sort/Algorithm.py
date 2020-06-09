set = [2, 1, 3, 44, 6, 1, 3, 88, 21, 2, 11, 52]

for j in range(1, len(set)):
    key = set[j]
    i = j-1
    while i >= 0 and set[i] > key:
        set[i+1] = set[i]
        i = i - 1
    set[i+1] = key


print(set)
