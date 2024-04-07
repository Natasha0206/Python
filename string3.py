# print all the vowels in the string "hayeram"

a = "hayeram"
v = ("a","e","i","o","u")
for i in range(len(a)):
    if a[i] in v:
        print(a[i])