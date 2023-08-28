def isPositive(i):
    if i > 0:
        return True
    return False

def isPalindrome(i):
    if int(str(i)[::-1]) is i:
        return True
    return False

N = int(input())
storage = map(int, input().split())
storage = sorted(storage)

if all([isPositive(i) for i in storage]):
    if any([isPalindrome(i) for i in storage]):
        print("True")
    else:
        print("False")
else:
    print("False")
