from datetime import datetime

def diff(t1,t2):
    t1m=datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2m=datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = str(int(abs((t1m - t2m).total_seconds())))
    return delta
with open('OutputFile.txt', 'w') as f:
        f.write("")
for i in range(int(input())):
    t1=input()
    t2=input()
    line=diff(t1,t2)
    with open('OutputFile.txt', 'a') as f:
        f.write(line + '\n')
with open('OutputFile.txt', 'r') as f:
    a=f.read()
    print(a, end='')
