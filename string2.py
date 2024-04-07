# you are given a string a="Everyone", print all the letters having an even index

a="Everyone"
for i in range(len(a)):
    if i%2==0:
        print(a[i])