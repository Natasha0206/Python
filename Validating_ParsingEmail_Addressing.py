from re import search

n = int(input())
line = ""
pattern = r"<[a-zA-Z]([\w\.\-])+@([a-zA-Z])+\.([a-zA-Z]){1,3}>$"

for _ in range(n):
    line = input()
    if search(pattern, line) is not None:
        print(line)