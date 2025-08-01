from itertools import combinations

word = 'BANANA'
Stuart = set()
for i in range(1, len(word) + 1):
    for combo in combinations(word, i):
        x = "".join(combo)
        print(x)