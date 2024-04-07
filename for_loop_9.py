#print numbers from 1-10, if number is 3,6,9 then skip the iteration

num = 0
for num in range(1,11):
    if num == 3 or num==6 or num == 9:
        continue
    print(num)