# you are given a string s = "hello there brother trucker",
# you need to capitalise every alphabet at an even 
# index of every word seperately and then print new string

s = "hello there brother trucker" 
l = s.split()
print(l)

for i in range(len(l)):
    m = list(l[i])
    for j in range(len(m)):
        if j%2==0:
            m[j] = m[j].upper()
    print(m)