def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in {'A','E','I','O','U'}:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)
    if stuart == kevin:
        print('Draw')
    elif stuart > kevin:
        print('Stuart',stuart)
    else:
        print('Kevin',kevin)
