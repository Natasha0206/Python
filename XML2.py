maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    # XML2 - Find the Maximum Depth in Python - Hacker Rank Solution START
    if (level == maxdepth):
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)
    # XML2 - Find the Maximum Depth in Python - Hacker Rank Solution END

