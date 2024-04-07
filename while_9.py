#print numbers from 1-10, if number is 3,6,9 then skip the iteration

num = 0
while 0<=num<10:
    num += 1
    if num == 3 or num == 6 or num == 9:
        continue
    print(num)