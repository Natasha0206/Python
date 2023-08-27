from itertools import combinations, groupby

# Read the input
count, letters, to_select = int(input()), input().split(), int(input())

# sort the letters so all a's are on left side
letters = sorted(letters)

# Find all possible combinations of to_select
combinations_of_letters = list(combinations(letters, to_select))

# find all which contain
contain = len([c for c in combinations_of_letters if 'a' in c])

# Print Results
print(contain / len(combinations_of_letters))
